import psycopg2
from psycopg2.extras import RealDictCursor

from webchecker import settings

db = psycopg2.connect(settings.DATABASE_URL, cursor_factory=RealDictCursor)
