from rest_framework import generics, permissions, status
from django.contrib.auth import get_user_model, authenticate
from .models import Incident, DailyAnalysis, MonthlyAnalysis
from .serializers import UserSerializer, IncidentSerializer, DailyAnalysisSerializer, MonthlyAnalysisSerializer
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render
from django.contrib.auth.hashers import make_password
from django.views.decorators.csrf import csrf_exempt


User = get_user_model()

class UserRegisterView(generics.CreateAPIView):
    """
    User registration endpoint.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        password = serializer.validated_data.get('password')
        serializer.save(password=make_password(password))

def home(request):
    """
    Home page view for the API.
    """
    api_urls = {
        'register': '/register/',
        'login': '/login/',
        'report': '/report/',
        'incidents': '/incidents/',
        'daily-analysis': '/daily-analysis/',  # (Admin only)
        'monthly-analysis': '/monthly-analysis/',  # (Admin only)
    }
    return render(request, 'home.html', context={'api_urls': api_urls})

class IncidentReportView(generics.CreateAPIView):
    
    """
    Incident report endpoint.
    """
    
    queryset = Incident.objects.all()
    serializer_class = IncidentSerializer
    permission_classes = []

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
class IncidentListView(generics.ListAPIView):
    """
    Retrieve all incident reports.
    """
    queryset = Incident.objects.all()
    serializer_class = IncidentSerializer
    permission_classes = []

class IncidentDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete an incident report.
    """
    queryset = Incident.objects.all()
    serializer_class = IncidentSerializer
    permission_classes = []
    
class LoginView(APIView):

    """
    User login endpoint.
    """
    
    @csrf_exempt
    def post(self, request, *args, **kwargs):
        username = request.data.get("username")
        password = request.data.get("password")
        user = User.objects.filter(username=username).first()
        if user and user.check_password(password):
            token, _ = Token.objects.get_or_create(user=user)
            user_data = UserSerializer(user).data
            return Response({
                "token": token.key,
                "user": user_data
            })
        return Response({"error": "Invalid Credentials"}, status=400)
    

class DailyAnalysisView(generics.ListAPIView):
    """
    List daily analysis data (Admin only).
    """
    queryset = DailyAnalysis.objects.all()
    serializer_class = DailyAnalysisSerializer
    permission_classes = []

class MonthlyAnalysisView(generics.ListAPIView):

    """
    List monthly analysis data (Admin only).
    """
    
    queryset = MonthlyAnalysis.objects.all()
    serializer_class = MonthlyAnalysisSerializer
    permission_classes = []
