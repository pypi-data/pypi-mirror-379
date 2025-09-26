import time
import logging
import os
from azure.storage.queue import QueueServiceClient
from .config import (
    SAS_TOKEN,
    STORAGE_ACCOUNT_NAME,
    STORAGE_QUEUE_NAME,
    TIMEOUT_DURATION,
    LOGSERV_LOG_INCLUDE_FILTERS,
    LOGSERV_LOG_EXCLUDE_FILTERS,
    LOG_LEVEL,
    OUTPUT_METHOD,
)
from .log_processor import process_log_file
from .message_processing import QueueMessageProcessor


RELEVANT_ENV_VARS = [
    "SAS_TOKEN",
    "STORAGE_ACCOUNT_NAME",
    "STORAGE_QUEUE_NAME",
    "OUTPUT_METHOD",
    "TIMEOUT_DURATION",
    "LOGSERV_LOG_INCLUDE_FILTERS",
    "LOGSERV_LOG_EXCLUDE_FILTERS",
    "HTTP_ENDPOINT",
    "TLS_CERT_PATH",
    "TLS_KEY_PATH",
    "AUTH_METHOD",
    "AUTH_TOKEN",
    "API_KEY",
    "OUTPUT_DIR",
    "COMPRESS_OUTPUT_FILE",
    "LOG_LEVEL",
]

MAX_RETRIES = 5  # Maximum number of retries for a message
CONSOLE_MODE = OUTPUT_METHOD == "console"


def set_log_level():
    """Set the log level based on the LOG_LEVEL config."""
    numeric_level = getattr(logging, LOG_LEVEL, logging.INFO)
    if CONSOLE_MODE:
        numeric_level = logging.ERROR
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(message)s",
        level=numeric_level,
    )
    logging.info("Log level set to %s", logging.getLevelName(numeric_level))


def log_env_vars():
    """Log relevant environment variables at DEBUG level."""
    logging.debug("Relevant environment variables:")
    for key in RELEVANT_ENV_VARS:
        logging.debug("%s=%s", key, os.getenv(key))

def has_timed_out(start_time, timeout_duration):
    if timeout_duration is None:
        return False
    return (time.time() - start_time) > timeout_duration

def is_relevant_blob_event(subject):
    subj = subject.lower()
    if "azure-webjobs-hosts" in subj:
        return False
    if "logserv" not in subj:
        return False
    if LOGSERV_LOG_EXCLUDE_FILTERS and any(ex in subj for ex in LOGSERV_LOG_EXCLUDE_FILTERS):
        return False
    if LOGSERV_LOG_INCLUDE_FILTERS:
        if not any(filt in subj for filt in LOGSERV_LOG_INCLUDE_FILTERS):
            return False
    return True

def consume_queue():
    set_log_level()
    log_env_vars()

    logging.info("Starting queue consumer...")
    account_url = f"https://{STORAGE_ACCOUNT_NAME}.queue.core.windows.net"
    queue_service = QueueServiceClient(account_url=account_url, credential=SAS_TOKEN)
    queue_client = queue_service.get_queue_client(STORAGE_QUEUE_NAME)

    processor = QueueMessageProcessor(
        queue_client,
        process_log_file=process_log_file,
        relevance_checker=is_relevant_blob_event,
        max_retries=MAX_RETRIES,
    )

    start_time = time.time()
    try:
        while True:
            if has_timed_out(start_time, TIMEOUT_DURATION):
                logging.info("Timeout reached. Exiting.")
                break

            messages = queue_client.receive_messages(messages_per_page=10, visibility_timeout=60)
            if not messages:
                logging.info("No messages in the queue. Waiting...")
                time.sleep(20)
                continue

            for message in messages:
                processor.process(message)

    except KeyboardInterrupt:
        logging.info("Forwarder stopped by user.")
    except Exception as e:
        logging.error("An error occurred: %s", e)


if __name__ == "__main__":
    consume_queue()
