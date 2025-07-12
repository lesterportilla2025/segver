from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Avg, Count
from django.utils import timezone
from datetime import datetime, timedelta
from rest_framework import views
from rest_framework.response import Response
import json
import random

from .models import QualityMetric, QualityAnalysis, AgentAlert

from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Avg, Count
from django.utils import timezone
from datetime import datetime, timedelta
from rest_framework import views
from rest_framework.response import Response
import json
import random

from .models import QualityMetric, QualityAnalysis, AgentAlert

def agent_dashboard(request):
    """Main dashboard for the quality analysis agent"""
    # Get recent metrics
    recent_metrics = QualityMetric.objects.all()[:10]
    
    # Get active alerts
    active_alerts = AgentAlert.objects.filter(is_resolved=False)[:5]
    
    # Get recent analyses
    recent_analyses = QualityAnalysis.objects.all()[:5]
    
    # Calculate summary statistics
    total_metrics = QualityMetric.objects.count()
    active_alerts_count = AgentAlert.objects.filter(is_resolved=False).count()
    critical_analyses = QualityAnalysis.objects.filter(status='critical').count()
    
    context = {
        'recent_metrics': recent_metrics,
        'active_alerts': active_alerts,
        'recent_analyses': recent_analyses,
        'total_metrics': total_metrics,
        'active_alerts_count': active_alerts_count,
        'critical_analyses': critical_analyses,
    }
    
    return render(request, 'quality_agent/dashboard.html', context)

def metrics_list(request):
    """Display list of quality metrics"""
    metrics = QualityMetric.objects.all()
    return render(request, 'quality_agent/metrics_list.html', {'metrics': metrics})

def alerts_list(request):
    """Display list of agent alerts"""
    alerts = AgentAlert.objects.all()
    return render(request, 'quality_agent/alerts_list.html', {'alerts': alerts})

class QualityAnalysisAPI(views.APIView):
    """API for performing quality analysis"""
    
    def post(self, request):
        """Perform automated quality analysis"""
        data = request.data
        metric_ids = data.get('metric_ids', [])
        
        if not metric_ids:
            # Analyze all recent metrics if none specified
            metrics = QualityMetric.objects.filter(
                date_recorded__gte=timezone.now() - timedelta(days=7)
            )
        else:
            metrics = QualityMetric.objects.filter(id__in=metric_ids)
        
        if not metrics.exists():
            return Response({'error': 'No metrics found for analysis'}, status=400)
        
        # Perform analysis
        analysis_result = self.analyze_metrics(metrics)
        
        # Create analysis record
        analysis = QualityAnalysis.objects.create(
            title=f"Análisis Automático - {timezone.now().strftime('%Y-%m-%d %H:%M')}",
            status=analysis_result['status'],
            recommendations=analysis_result['recommendations'],
            confidence_score=analysis_result['confidence_score']
        )
        
        # Add metrics to the analysis
        analysis.metrics.set(metrics)
        
        # Create alerts if necessary
        if analysis_result['status'] in ['warning', 'critical']:
            self.create_alerts(metrics, analysis_result)
        
        return Response({
            'analysis_id': analysis.id,
            'status': analysis_result['status'],
            'recommendations': analysis_result['recommendations'],
            'confidence_score': analysis_result['confidence_score']
        })
    
    def analyze_metrics(self, metrics):
        """Perform the actual analysis logic"""
        total_metrics = len(metrics)
        metrics_below_target = 0
        recommendations = []
        
        for metric in metrics:
            # Simple analysis: check if metric is below target
            if metric.value < metric.target_value:
                metrics_below_target += 1
                deviation = ((metric.target_value - metric.value) / metric.target_value) * 100
                recommendations.append(
                    f"• {metric.name}: Está {deviation:.1f}% por debajo del objetivo. "
                    f"Valor actual: {metric.value}{metric.unit}, Objetivo: {metric.target_value}{metric.unit}"
                )
        
        # Determine status based on percentage of metrics below target
        percentage_below = (metrics_below_target / total_metrics) * 100
        
        if percentage_below == 0:
            status = 'good'
            recommendations.insert(0, "✅ Todas las métricas están cumpliendo con los objetivos.")
        elif percentage_below <= 30:
            status = 'warning'
            recommendations.insert(0, f"⚠️  {percentage_below:.1f}% de las métricas necesitan atención.")
        else:
            status = 'critical'
            recommendations.insert(0, f"🚨 {percentage_below:.1f}% de las métricas están por debajo del objetivo. Se requiere acción inmediata.")
        
        # Add general recommendations
        if status != 'good':
            recommendations.extend([
                "• Revisar los procesos relacionados con las métricas afectadas",
                "• Implementar medidas correctivas inmediatas",
                "• Aumentar la frecuencia de monitoreo",
                "• Considerar ajustar los objetivos si son poco realistas"
            ])
        
        # Calculate confidence score (simplified)
        confidence_score = max(0.5, 1.0 - (percentage_below / 100))
        
        return {
            'status': status,
            'recommendations': '\n'.join(recommendations),
            'confidence_score': confidence_score
        }
    
    def create_alerts(self, metrics, analysis_result):
        """Create alerts for problematic metrics"""
        for metric in metrics:
            if metric.value < metric.target_value:
                deviation = ((metric.target_value - metric.value) / metric.target_value) * 100
                
                if deviation > 50:
                    priority = 'urgent'
                    alert_type = 'threshold'
                elif deviation > 25:
                    priority = 'high'
                    alert_type = 'threshold'
                else:
                    priority = 'medium'
                    alert_type = 'threshold'
                
                AgentAlert.objects.create(
                    alert_type=alert_type,
                    priority=priority,
                    message=f"La métrica '{metric.name}' está {deviation:.1f}% por debajo del objetivo.",
                    metric=metric
                )

@csrf_exempt
def add_sample_data(request):
    """Add sample data for testing (remove in production)"""
    if request.method == 'POST':
        # Create sample metrics
        sample_metrics = [
            {'name': 'Tasa de Defectos', 'type': 'defect_rate', 'value': 2.5, 'target': 2.0, 'unit': '%'},
            {'name': 'Cumplimiento de Entregas', 'type': 'compliance', 'value': 95.0, 'target': 98.0, 'unit': '%'},
            {'name': 'Eficiencia de Proceso', 'type': 'efficiency', 'value': 88.0, 'target': 90.0, 'unit': '%'},
            {'name': 'Satisfacción del Cliente', 'type': 'customer_satisfaction', 'value': 4.2, 'target': 4.5, 'unit': '/5'},
            {'name': 'Tiempo de Procesamiento', 'type': 'process_time', 'value': 12.5, 'target': 10.0, 'unit': 'horas'},
        ]
        
        for metric_data in sample_metrics:
            QualityMetric.objects.create(
                name=metric_data['name'],
                metric_type=metric_data['type'],
                value=metric_data['value'],
                target_value=metric_data['target'],
                unit=metric_data['unit'],
                recorded_by_id=1  # Assuming user with ID 1 exists
            )
        
        return JsonResponse({'message': 'Datos de ejemplo agregados exitosamente'})
    
    return JsonResponse({'error': 'Método no permitido'}, status=405)
