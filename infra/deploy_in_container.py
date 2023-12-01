import logging
import os
import time

import psycopg2
from decouple import config

logging.basicConfig(
    level=logging.DEBUG, format='[%(asctime)s] [%(levelname)s] %(message)s'
)
logger = logging.getLogger(__name__)

logger.debug('Waiting for database connection')
while True:
    try:
        psycopg2.connect(
            host=config('DB_HOST'),
            port=config('DB_PORT'),
            password=config('POSTGRES_PASSWORD'),
            user=config('POSTGRES_USER'),
        )
        logger.debug('Successful connection')
        break
    except psycopg2.OperationalError:
        logger.info('No connection to database, connection restarted')
        time.sleep(5)
os.system('python manage.py makemigrations')
os.system('python manage.py migrate')
os.system('python manage.py collectstatic --noinput')
os.system('python manage.py loaddata dumpdata/db.json')
os.system('gunicorn shop.wsgi:application --bind 0:8000')
