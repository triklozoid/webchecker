import json
import logging
import os
import time

import requests
from kafka import KafkaProducer

# import logger

log = logging.getLogger(__name__)

sites = ['https://google.com', 'https://yandex.ru']

bootstrap_servers = "{}:{}".format(os.getenv('KAFKA_HOST'), os.getenv('KAFKA_PORT'))

producer = KafkaProducer(
    bootstrap_servers=bootstrap_servers,
    security_protocol="SSL",
    ssl_cafile="/code/certs/ca.pem",
    ssl_certfile="/code/certs/service.cert",
    ssl_keyfile="/code/certs/service.key",
)


def check(site):
    result = requests.get(site)
    log.info(result)
    message = {'status_code': result.status_code, 'site': site}
    producer.send('test', json.dumps(message).encode('utf-8'))


def run_producer():
    while True:
        for site in sites:
            check(site)

        time.sleep(10)
