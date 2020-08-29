import os

from kafka import KafkaConsumer, KafkaProducer

bootstrap_servers = "{}:{}".format(os.getenv("KAFKA_HOST"), os.getenv("KAFKA_PORT"))

consumer = KafkaConsumer(
    "test",
    auto_offset_reset="earliest",
    bootstrap_servers=bootstrap_servers,
    client_id="demo-client-1",
    group_id="demo-group",
    security_protocol="SSL",
    ssl_cafile="/code/certs/ca.pem",
    ssl_certfile="/code/certs/service.cert",
    ssl_keyfile="/code/certs/service.key",
)

producer = KafkaProducer(
    bootstrap_servers=bootstrap_servers,
    security_protocol="SSL",
    ssl_cafile="/code/certs/ca.pem",
    ssl_certfile="/code/certs/service.cert",
    ssl_keyfile="/code/certs/service.key",
)
