import json
import logging
import os
import time

import requests
from kafka import KafkaProducer

from webchecker.database import db
from webchecker.kafka import producer
from webchecker.schemas import Metric, Site

log = logging.getLogger(__name__)


def check(site: Site):
    try:
        result = requests.get(site.url, timeout=5)
    except Exception as e:
        metric = Metric(
            site_id=site.id,
            error=e.__class__.__name__,
        )
    else:
        metric = Metric(
            status_code=result.status_code,
            site_id=site.id,
            request_time=result.elapsed.total_seconds(),
        )
    log.info(metric)
    return metric


def get_sites():
    with db.cursor() as c:
        c.execute("select id, url from sites")
        for site_data in c:
            yield Site(**site_data)


def run_producer():
    while True:
        for site in get_sites():
            metric = check(site)
            producer.send("test", metric.json().encode("utf-8"))

        time.sleep(10)
