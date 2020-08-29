import os

import psycopg2
from psycopg2.extras import RealDictCursor

uri = os.getenv('DATABASE_URL')
db = psycopg2.connect(uri, cursor_factory=RealDictCursor)
