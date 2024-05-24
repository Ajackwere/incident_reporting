from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


class User(AbstractUser):
    phone_number = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.username

class Incident(models.Model):
    INCIDENT_TYPES = [
        ('No water', 'No water'),
        ('Vandalism', 'Vandalism'),
        ('Leaks and Bursts', 'Leaks and Bursts'),
        ('Meter Theft', 'Meter Theft'),
        ('HR Issue', 'HR Issue'),
        ('OSH Activity', 'OSH Activity'),
    ]

    LOCATIONS = [
        ('Milimani', 'Milimani'),
        ('CBD', 'CBD'),
        ('Riat', 'Riat'),
        ('Manyatta', 'Manyatta'),
        ('Kenya Re', 'Kenya Re'),
        ('Head Office', 'Head Office'),
        ('Kibuye', 'Kibuye'),
        ('Kisat', 'Kisat'),
        ('Kajulu', 'Kajulu'),
    ]


    user = models.ForeignKey(User, on_delete=models.CASCADE)
    incident_type = models.CharField(max_length=50, choices=INCIDENT_TYPES)
    location = models.CharField(max_length=50, choices=LOCATIONS)
    description = models.TextField()
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.incident_type} reported by {self.user.username}"
    
class DailyAnalysis(models.Model):
    date = models.DateField()
    total_incidents = models.PositiveIntegerField()
    incidents_per_type = models.JSONField()  

    def __str__(self):
        return f"Daily Analysis for {self.date}"

class MonthlyAnalysis(models.Model):
    month = models.DateField()
    total_incidents = models.PositiveIntegerField()
    incidents_per_type = models.JSONField()

    def __str__(self):
        return f"Monthly Analysis for {self.month}"
        

