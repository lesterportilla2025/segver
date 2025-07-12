from django.contrib import admin
from .models import QualityMetric, QualityAnalysis, AgentAlert

@admin.register(QualityMetric)
class QualityMetricAdmin(admin.ModelAdmin):
    list_display = ['name', 'metric_type', 'value', 'target_value', 'unit', 'date_recorded', 'recorded_by']
    list_filter = ['metric_type', 'date_recorded']
    search_fields = ['name']
    ordering = ['-date_recorded']

@admin.register(QualityAnalysis)
class QualityAnalysisAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'confidence_score', 'analysis_date']
    list_filter = ['status', 'analysis_date']
    search_fields = ['title']
    ordering = ['-analysis_date']

@admin.register(AgentAlert)
class AgentAlertAdmin(admin.ModelAdmin):
    list_display = ['alert_type', 'priority', 'metric', 'is_resolved', 'created_at']
    list_filter = ['alert_type', 'priority', 'is_resolved', 'created_at']
    search_fields = ['message']
    ordering = ['-created_at']
