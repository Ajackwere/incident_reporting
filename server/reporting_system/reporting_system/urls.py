from django.contrib import admin
from django.urls import path
from reports.views import UserRegisterView, IncidentReportView, LoginView, DailyAnalysisView, MonthlyAnalysisView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('report/', IncidentReportView.as_view(), name='report'),
    path('daily-analysis/', DailyAnalysisView.as_view(), name='daily_analysis'),
    path('monthly-analysis/', MonthlyAnalysisView.as_view(), name='monthly_analysis'),
    path('admin/', admin.site.urls),
]
