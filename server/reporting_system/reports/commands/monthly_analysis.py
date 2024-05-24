from django.core.management.base import BaseCommand
from django.utils import timezone
from django.db.models import Count
from incidents.models import Incident, MonthlyAnalysis
from collections import Counter

class Command(BaseCommand):
    help = 'Generate monthly analysis of incidents'

    def handle(self, *args, **kwargs):
        today = timezone.now().date()
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

        self.stdout.write(self.style.SUCCESS(f'Monthly analysis for {start_of_month} completed successfully'))
