from __future__ import absolute_import, unicode_literals
import os
from reporting_system.celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'reporting_system.settings')

app = Celery('reporting_system')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
