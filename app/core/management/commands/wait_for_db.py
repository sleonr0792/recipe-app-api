import time

from django.db import connections
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """ django command to pause"""

    def handle(self, *args, **kwargs):
        self.stdout.write('waiting from db...')
        db_conn = None
        while not db_conn:
            try:
                db_conn = connections['default']
            except OperationalError:
                self.stdout.write('database unavailable , waiting a second')
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS('database available!'))
