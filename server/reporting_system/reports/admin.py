from django.contrib import admin
from .models import User, Incident, DailyAnalysis, MonthlyAnalysis
from django_celery_beat.models import PeriodicTask, CrontabSchedule

admin.site.register(User)
admin.site.register(Incident)
admin.site.register(DailyAnalysis)
admin.site.register(MonthlyAnalysis)
admin.site.register(PeriodicTask)
admin.site.register(CrontabSchedule)