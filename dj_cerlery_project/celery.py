from __future__ import absolute_import, unicode_literals
import os

from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dj_cerlery_project.settings')

app = Celery('dj_cerlery_project')

app.conf.enable_utc = False

app.conf.update(timezone='Africa/Nairobi')

app.config_from_object('django.conf:settings', namespace='CELERY')

#celery beat settings
app.conf.beat_schedule = {
    
}

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')