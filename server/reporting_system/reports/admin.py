from django.contrib import admin
from .models import User, Incident, DailyAnalysis, MonthlyAnalysis

class IncidentAdmin(admin.ModelAdmin):
    list_display = ('incident_type', 'location', 'user', 'date', 'time')
    search_fields = ('incident_type', 'location', 'user__username', 'date')
    list_filter = ('incident_type', 'location', 'date')

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['user'].queryset = User.objects.all()
        return form

admin.site.register(Incident, IncidentAdmin)
admin.site.register(User)
admin.site.register(DailyAnalysis)
admin.site.register(MonthlyAnalysis)
