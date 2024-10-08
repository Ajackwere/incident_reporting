from django.contrib import admin
from django.urls import path, include
from reports.views import UserRegisterView, IncidentReportView, LoginView, DailyAnalysisView, MonthlyAnalysisView, IncidentListView, IncidentDetailView, home
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Reporting System API",
        default_version='v1',
        description="API for reporting system",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="austinejackwere@gmai.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('', home, name='home'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('report/', IncidentReportView.as_view(), name='report'),
    path('incidents/', IncidentListView.as_view(), name='incident-list'),
    path('incidents/<int:pk>/', IncidentDetailView.as_view(), name='incident-detail'),
    path('daily-analysis/', DailyAnalysisView.as_view(), name='daily_analysis'),
    path('monthly-analysis/', MonthlyAnalysisView.as_view(), name='monthly_analysis'),
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    
]
