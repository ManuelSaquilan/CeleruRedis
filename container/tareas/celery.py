from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from tareas import settings


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tareas.settings')

app = Celery('tareas')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

