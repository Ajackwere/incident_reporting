from celery import shared_task
from django.core.management import call_command

@shared_task
def run_daily_analysis():
    call_command('daily_analysis')

@shared_task
def run_monthly_analysis():
    call_command('monthly_analysis')
