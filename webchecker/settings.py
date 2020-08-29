import os

KAFKA_BOOTSTRAP_SERVERS = "{}:{}".format(
    os.getenv("KAFKA_HOST"), os.getenv("KAFKA_PORT")
)
DATABASE_URL = os.getenv("DATABASE_URL")

SITE_CHECK_TIMEOUT = 5
SLEEP_AFTER_CHECK = 10

KAFKA_METRICS_TOPIC = "metrics"
