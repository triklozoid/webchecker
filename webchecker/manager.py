import logging

from psycopg2.errors import UniqueViolation

from webchecker.database import db

log = logging.getLogger(__name__)


def add_site(args):
    with db.cursor() as c:
        try:
            c.execute(
                "INSERT INTO sites (url ) VALUES (%s )",
                (args.url,),
            )
        except UniqueViolation:
            log.error("Site with url {} already exists".format(args.url))
    db.commit()
