import logging

from webchecker.database import db
from webchecker.kafka import consumer
from webchecker.schemas import Metric

log = logging.getLogger(__name__)


def run_consumer(args):
    while True:
        raw_msgs = consumer.poll(timeout_ms=1000)
        for tp, msgs in raw_msgs.items():
            for msg in msgs:
                log.info("Received: {}".format(msg.value))
                metric = Metric.parse_raw(msg.value)

                with db.cursor() as c:
                    c.execute(
                        "INSERT INTO metrics (site_id, status_code, request_time, error) VALUES (%s, %s, %s, %s)",
                        (
                            metric.site_id,
                            metric.status_code,
                            metric.request_time,
                            metric.error,
                        ),
                    )
        db.commit()
