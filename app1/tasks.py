from __future__ import absolute_import, unicode_literals

from celery import shared_task
from celery import Celery

app = Celery('tasks', backend='rpc://',broker='pyamqp://')
@app.task
def add(x,y):
    c = x+y
    return c