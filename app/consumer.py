import json
import os

import psycopg2
from kafka import KafkaConsumer
from psycopg2.extras import RealDictCursor

bootstrap_servers = "{}:{}".format(os.getenv('KAFKA_HOST'), os.getenv('KAFKA_PORT'))

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


uri = os.getenv('POSTGRESQL_URI')

db_conn = psycopg2.connect(uri)
c = db_conn.cursor(cursor_factory=RealDictCursor)

while True:
    raw_msgs = consumer.poll(timeout_ms=1000)
    for tp, msgs in raw_msgs.items():
        for msg in msgs:
            msg_dict = json.loads(msg.value)
            c.execute(
                "INSERT INTO sites (site, status_code) VALUES (%s, %s)",
                (msg_dict["site"], msg_dict['status_code']),
            )
            print("Received: {}".format(msg_dict))

    db_conn.commit()

consumer.commit()
