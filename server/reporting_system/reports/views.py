from rest_framework import generics, permissions
from django.contrib.auth import get_user_model
from .models import Incident, DailyAnalysis, MonthlyAnalysis
from .serializers import UserSerializer, IncidentSerializer, DailyAnalysisSerializer, MonthlyAnalysisSerializer
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView

User = get_user_model()

class UserRegisterView(generics.CreateAPIView):
    """
    User registration endpoint.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class IncidentReportView(generics.CreateAPIView):
    
    """
    Incident report endpoint.
    """
    
    queryset = Incident.objects.all()
    serializer_class = IncidentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class LoginView(APIView):

    """
    User login endpoint.
    """
    
    def post(self, request, *args, **kwargs):
        username = request.data.get("username")
        password = request.data.get("password")
        user = User.objects.filter(username=username).first()
        if user and user.check_password(password):
            token, _ = Token.objects.get_or_create(user=user)
            return Response({"token": token.key})
        return Response({"error": "Invalid Credentials"}, status=400)

class DailyAnalysisView(generics.ListAPIView):
    """
    List daily analysis data (Admin only).
    """
    queryset = DailyAnalysis.objects.all()
    serializer_class = DailyAnalysisSerializer
    permission_classes = [permissions.IsAdminUser]

class MonthlyAnalysisView(generics.ListAPIView):

    """
    List monthly analysis data (Admin only).
    """
    
    queryset = MonthlyAnalysis.objects.all()
    serializer_class = MonthlyAnalysisSerializer
    permission_classes = [permissions.IsAdminUser]
