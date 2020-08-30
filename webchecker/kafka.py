from kafka import KafkaConsumer, KafkaProducer

from webchecker import settings

consumer = KafkaConsumer(
    settings.KAFKA_METRICS_TOPIC,
    auto_offset_reset="earliest",
    bootstrap_servers=settings.KAFKA_BOOTSTRAP_SERVERS,
    client_id="demo-client-1",
    group_id="demo-group",
    security_protocol="SSL",
    ssl_cafile="./certs/ca.pem",
    ssl_certfile="./certs/service.cert",
    ssl_keyfile="./certs/service.key",
)

producer = KafkaProducer(
    bootstrap_servers=settings.KAFKA_BOOTSTRAP_SERVERS,
    security_protocol="SSL",
    ssl_cafile="./certs/ca.pem",
    ssl_certfile="./certs/service.cert",
    ssl_keyfile="./certs/service.key",
)
