import base64
import json
import logging
from typing import Callable

from azure.core.exceptions import HttpResponseError, ResourceNotFoundError


def format_metadata(metadata):
    formatted = {}
    for key, value in metadata.items():
        formatted[key] = value.isoformat() if hasattr(value, "isoformat") else value
    payload = json.dumps(formatted, sort_keys=True, indent=2, default=str)
    return "  " + payload.replace("\n", "\n  ")


def log_message_metadata(message, prefix=""):
    prefix_text = f"{prefix} - " if prefix else ""
    metadata = {
        "id": getattr(message, "id", None),
        "dequeue_count": getattr(message, "dequeue_count", None),
        "pop_receipt": getattr(message, "pop_receipt", None),
        "next_visible_on": getattr(
            message,
            "next_visible_on",
            getattr(message, "time_next_visible", None),
        ),
        "inserted_on": getattr(
            message,
            "inserted_on",
            getattr(message, "insertion_time", None),
        ),
        "expires_on": getattr(
            message,
            "expires_on",
            getattr(message, "expiration_time", None),
        ),
    }
    logging.debug("%sMessage metadata:\n%s", prefix_text, format_metadata(metadata))


def handle_message_not_found(error, message, action):
    error_code = getattr(error, "error_code", None)
    status_code = getattr(error, "status_code", None)
    if error_code == "MessageNotFound" or status_code == 404:
        logging.debug(
            "Message id=%s missing during %s (error_code=%s, status_code=%s).",
            getattr(message, "id", None),
            action,
            error_code,
            status_code,
        )
        return True
    return False


def delete_message(queue_client, message, reason, log_success=False):
    logging.debug(
        "Deleting message id=%s (reason=%s) with pop_receipt=%s",
        getattr(message, "id", None),
        reason,
        getattr(message, "pop_receipt", None),
    )
    try:
        queue_client.delete_message(message)
        deleted = True
    except (ResourceNotFoundError, HttpResponseError) as err:
        deleted = handle_message_not_found(err, message, f"delete:{reason}")
        if not deleted:
            raise
    if deleted:
        logging.debug("Message deleted.")
        if log_success:
            logging.info("Message processed and deleted: %s", getattr(message, "id", None))
    return deleted


class QueueMessageProcessor:
    def __init__(
        self,
        queue_client,
        *,
        process_log_file: Callable[[str], None],
        relevance_checker: Callable[[str], bool],
        max_retries: int,
    ) -> None:
        self.queue_client = queue_client
        self.process_log_file = process_log_file
        self.relevance_checker = relevance_checker
        self.max_retries = max_retries

    def process(self, message) -> None:
        log_message_metadata(message, prefix="Received")
        decoded_text, message_content = self._decode_message_content(message)
        if message_content is None:
            delete_message(self.queue_client, message, reason="decode-error")
            return

        skip_reason, skip_log = self._should_skip_message(message_content)
        if skip_reason:
            if skip_log:
                logging.debug(skip_log)
            delete_message(self.queue_client, message, reason=skip_reason)
            return

        retry_count = int(message_content.get("retry_count", 0))
        if retry_count >= self.max_retries:
            logging.error("Max retries reached for message: %s. Deleting message.", message.id)
            delete_message(self.queue_client, message, reason="max-retries")
            return

        blob_url = message_content.get("data", {}).get("url", "")
        if not blob_url:
            logging.error("No blob URL found in message: %s - %s", message.id, decoded_text)
            delete_message(self.queue_client, message, reason="missing-blob-url")
            return

        self._process_blob(message, blob_url, retry_count, message_content)

    def _decode_message_content(self, message):
        try:
            decoded_message = base64.b64decode(message.content).decode("utf-8")
            return decoded_message, json.loads(decoded_message)
        except Exception as exc:  # pragma: no cover - defensive
            logging.error("Failed to decode message: %s - Message content: %s", exc, message.content)
            return None, None

    def _should_skip_message(self, message_content):
        event_type = message_content.get("eventType", "")
        subject = message_content.get("subject", "")
        if event_type != "Microsoft.Storage.BlobCreated" or not self.relevance_checker(subject):
            log = (
                f"Irrelevant message: event_type={event_type}, subject={subject}. Skipping message."
            )
            return "irrelevant", log
        return None, None

    def _process_blob(self, message, blob_url, retry_count, message_content):
        try:
            logging.info("Processing message: %s - %s", message.id, blob_url)
            self.process_log_file(blob_url)
            delete_message(
                self.queue_client,
                message,
                reason="processed",
                log_success=True,
            )
        except Exception as exc:  # pragma: no cover - exercised via tests
            self._handle_processing_failure(message, retry_count, message_content, exc)

    def _handle_processing_failure(self, message, retry_count, message_content, error):
        error_metadata = {
            "dequeue_count": getattr(message, "dequeue_count", None),
            "pop_receipt": getattr(message, "pop_receipt", None),
            "next_visible_on": getattr(
                message,
                "next_visible_on",
                getattr(message, "time_next_visible", None),
            ),
            "retry_count": retry_count,
        }
        logging.error(
            "Error processing message %s: %s | metadata:\n%s",
            message.id,
            error,
            format_metadata(error_metadata),
        )
        message_content["retry_count"] = retry_count + 1
        updated_message = base64.b64encode(json.dumps(message_content).encode("utf-8")).decode("utf-8")
        try:
            self.queue_client.update_message(
                message,
                content=updated_message,
                visibility_timeout=60,
            )
        except (ResourceNotFoundError, HttpResponseError) as err:
            if not handle_message_not_found(err, message, "update"):
                raise
