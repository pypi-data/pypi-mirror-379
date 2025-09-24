import os


def env_bool(name: str, default: bool = False) -> bool:
    v = os.getenv(name)
    if v is None:
        return default
    return v.lower() in ("1", "true", "yes", "on")


KAFKA_COMMON = {
    "bootstrap_servers": os.getenv("KAFKA_BOOTSTRAP_SERVERS", "localhost:9092"),
    "security_protocol": os.getenv("KAFKA_SECURITY_PROTOCOL", "SASL_SSL"),
    "sasl_mechanism": os.getenv("KAFKA_SASL_MECHANISM", "PLAIN"),
    "sasl_plain_username": os.getenv("KAFKA_SASL_USERNAME", ""),
    "sasl_plain_password": os.getenv("KAFKA_SASL_PASSWORD", ""),
    "client_id": os.getenv("KAFKA_CLIENT_ID", "market-data-service"),
}

PRODUCER_TUNING = {
    "acks": os.getenv("KAFKA_ACKS", "all"),
    "enable_idempotence": env_bool("KAFKA_ENABLE_IDEMPOTENCE", True),
    "linger_ms": int(os.getenv("KAFKA_LINGER_MS", "5")),
    "batch_size": int(os.getenv("KAFKA_BATCH_SIZE", "131072")),  # 128 KiB
    "compression_type": os.getenv("KAFKA_COMPRESSION_TYPE", "snappy"),
    "request_timeout_ms": int(os.getenv("KAFKA_REQUEST_TIMEOUT_MS", "30000")),
    "delivery_timeout_ms": int(os.getenv("KAFKA_DELIVERY_TIMEOUT_MS", "120000")),
    "reconnect_backoff_ms": 100,
    "reconnect_backoff_max_ms": 10000,
    "retry_backoff_ms": 100,
}

CONSUMER_TUNING = {
    "enable_auto_commit": env_bool("KAFKA_ENABLE_AUTO_COMMIT", False),
    "auto_offset_reset": os.getenv("KAFKA_AUTO_OFFSET_RESET", "latest"),
    "max_poll_interval_ms": int(os.getenv("KAFKA_MAX_POLL_INTERVAL_MS", "300000")),
    "session_timeout_ms": int(os.getenv("KAFKA_SESSION_TIMEOUT_MS", "45000")),
    "max_poll_records": int(os.getenv("KAFKA_MAX_POLL_RECORDS", "1000")),
    # при необходимости:
    # "fetch_max_bytes": int(os.getenv("KAFKA_FETCH_MAX_BYTES", "52428800")), # 50MB
    # "max_partition_fetch_bytes": int(os.getenv(
    #     "KAFKA_MAX_PART_FETCH_BYTES", "8388608"
    # )),  # 8MB
}
