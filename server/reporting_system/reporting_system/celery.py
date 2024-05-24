from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'reporting_system.settings')

app = Celery('reporting_system')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

# app.conf.update(
#     result_expires=3600,
# )

if __name__ == '__main__':
    app.start()