from rest_framework import serializers
from .models import User, Incident, DailyAnalysis, MonthlyAnalysis

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'phone_number']

class IncidentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Incident
        fields = ['id', 'user', 'incident_type', 'location', 'description', 'date', 'time']

class DailyAnalysisSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyAnalysis
        fields = ['id', 'date', 'total_incidents', 'incidents_per_type']

class MonthlyAnalysisSerializer(serializers.ModelSerializer):
    class Meta:
        model = MonthlyAnalysis
        fields = ['id', 'month', 'total_incidents', 'incidents_per_type']
