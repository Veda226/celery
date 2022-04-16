from __future__ import absolute_import, unicode_literals
from django.conf import settings
import os
from celery import Celery
from celery import shared_task
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proj.settings')

app = Celery('proj',backend='rpc://',broker='pyamqp://guest:guest@localhost:5672//',include=['app1.tasks'])

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
