from __future__ import absolute_import, unicode_literals
import os

from celery import Celery
from celery.schedules import crontab
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CORE.settings')

app = Celery('CORE')

app.conf.enable_utc = False

app.conf.update(timezone='Africa/Nairobi')

app.config_from_object('django.conf:settings', namespace='CELERY')

#celery beat settings for scheduling
app.conf.beat_schedule = {
    'send-mail-every-day-at-8': {
        'task': 'send_mail_app.tasks.send_mail_func',
        'schedule':  crontab(hour=11, minute=00),
        #'args': (2,)
    }
}

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')