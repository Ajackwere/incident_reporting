from django.contrib import admin
from .models import User, Incident, DailyAnalysis, MonthlyAnalysis
admin.site.register(User)
admin.site.register(Incident)
admin.site.register(DailyAnalysis)
admin.site.register(MonthlyAnalysis)
