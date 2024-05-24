from django.core.management.base import BaseCommand
from django.utils import timezone
from incidents.models import Incident, DailyAnalysis
from collections import Counter

class Command(BaseCommand):
    help = 'Generate daily analysis of incidents'

    def handle(self, *args, **kwargs):
        today = timezone.now().date()
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

        self.stdout.write(self.style.SUCCESS(f'Daily analysis for {today} completed successfully'))
