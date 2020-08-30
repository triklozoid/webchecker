import logging

from psycopg2.extras import execute_values

from webchecker.database import db
from webchecker.kafka import consumer
from webchecker.schemas import Metric

log = logging.getLogger(__name__)


def run_consumer(args):
    while True:
        raw_msgs = consumer.poll(timeout_ms=1000)
        for tp, msgs in raw_msgs.items():
            values = []
            for msg in msgs:
                log.info("Received: {}".format(msg.value))
                metric = Metric.parse_raw(msg.value)
                values.append(
                    (
                        metric.site_id,
                        metric.status_code,
                        metric.request_time,
                        metric.error,
                    )
                )

            with db.cursor() as c:
                # https://stackoverflow.com/questions/8134602/psycopg2-insert-multiple-rows-with-one-query
                execute_values(
                    c,
                    "INSERT INTO metrics (site_id, status_code, request_time, error) VALUES %s",
                    values,
                )
            log.info('commit')
            db.commit()
