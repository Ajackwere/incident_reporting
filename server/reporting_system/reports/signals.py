from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from .models import Incident, DailyAnalysis, MonthlyAnalysis
from collections import Counter

@receiver(post_save, sender=Incident)
def update_daily_analysis(sender, instance, created, **kwargs):
    if created:
        today = instance.date
        incidents = Incident.objects.filter(date=today)

        total_incidents = incidents.count()
        incidents_per_type = Counter(incidents.values_list('incident_type', flat=True))

        DailyAnalysis.objects.update_or_create(
            date=today,
            defaults={
                'total_incidents': total_incidents,
                'incidents_per_type': dict(incidents_per_type),
            }
        )

@receiver(post_save, sender=Incident)
def update_monthly_analysis(sender, instance, created, **kwargs):
    if created:
        today = instance.date
        start_of_month = today.replace(day=1)

        incidents = Incident.objects.filter(date__gte=start_of_month, date__lte=today)

        total_incidents = incidents.count()
        incidents_per_type = Counter(incidents.values_list('incident_type', flat=True))

        MonthlyAnalysis.objects.update_or_create(
            month=start_of_month,
            defaults={
                'total_incidents': total_incidents,
                'incidents_per_type': dict(incidents_per_type),
            }
        )
