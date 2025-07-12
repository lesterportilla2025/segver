from django.urls import path
from . import views

app_name = 'quality_agent'

urlpatterns = [
    path('', views.agent_dashboard, name='dashboard'),
    path('metrics/', views.metrics_list, name='metrics_list'),
    path('alerts/', views.alerts_list, name='alerts_list'),
    path('api/analyze/', views.QualityAnalysisAPI.as_view(), name='analyze_api'),
    path('api/sample-data/', views.add_sample_data, name='add_sample_data'),
]