import json
import logging
import os
import time

import requests
from kafka import KafkaProducer

from webchecker.database import db
from webchecker.kafka import producer
from webchecker.schemas import Site

log = logging.getLogger(__name__)


def check(site: Site):
    result = requests.get(site.url)
    log.info(result)
    message = {"status_code": result.status_code, "site_id": site.id}
    producer.send("test", json.dumps(message).encode("utf-8"))


def get_sites():
    with db.cursor() as c:
        c.execute("select id, url from sites")
        for site_data in c:
            yield Site(**site_data)


def run_producer():
    while True:
        for site in get_sites():
            check(site)

        time.sleep(10)
