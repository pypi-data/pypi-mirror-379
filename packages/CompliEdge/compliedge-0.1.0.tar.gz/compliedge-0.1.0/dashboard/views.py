from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Q
from django.utils import timezone
from datetime import datetime, timedelta
from users.models import User
from governance.models import Policy
from risk.models import Risk, RiskCategory
from compliance.models import ComplianceChecklist, ComplianceAudit, ComplianceFramework
from permissions.decorators import admin_required, manager_required, auditor_required, employee_required
from ai.risk_predictor import RiskPredictor
from ai.compliance_checker import ComplianceChecker

@login_required
def home(request):
    """
    Main dashboard view with overview of all modules
    """
    # User statistics (only for Admin)
    total_users = 0
    users_by_role = []
    if request.user.role == User.Role.ADMIN:
        total_users = User.objects.count()
        users_by_role = User.objects.values('role').annotate(count=Count('role'))
    
    # Policy statistics
    total_policies = Policy.objects.count()
    policies_by_status = Policy.objects.values('status').annotate(count=Count('status'))
    
    # Risk statistics
    total_risks = Risk.objects.count()
    risks_by_priority = Risk.objects.values('priority').annotate(count=Count('priority'))
    risks_by_status = Risk.objects.values('status').annotate(count=Count('status'))
    
    # Compliance statistics
    total_checklists = ComplianceChecklist.objects.count()
    checklists_by_status = ComplianceChecklist.objects.values('status').annotate(count=Count('status'))
    total_audits = ComplianceAudit.objects.count()
    
    # AI Predictions and Suggestions
    ai_predictions = RiskPredictor.predict_risks()
    ai_compliance_risks = RiskPredictor.predict_policy_compliance_risks()
    ai_suggestions = RiskPredictor.get_ai_suggestions(request.user)
    
    context = {
        'total_users': total_users,
        'users_by_role': users_by_role,
        'total_policies': total_policies,
        'policies_by_status': policies_by_status,
        'total_risks': total_risks,
        'risks_by_priority': risks_by_priority,
        'risks_by_status': risks_by_status,
        'total_checklists': total_checklists,
        'checklists_by_status': checklists_by_status,
        'total_audits': total_audits,
        'ai_predictions': ai_predictions[:3],  # Show top 3 predictions
        'ai_compliance_risks': ai_compliance_risks[:3],  # Show top 3 compliance risks
        'ai_suggestions': ai_suggestions[:3]  # Show top 3 suggestions
    }
    
    return render(request, 'dashboard/home.html', context)

@login_required
def analytics(request):
    """
    Detailed analytics dashboard with charts and graphs
    """
    # Get date range for trend analysis (last 30 days)
    end_date = timezone.now().date()
    start_date = end_date - timedelta(days=30)
    
    # Risk trend analysis
    risk_trend_data = []
    current_date = start_date
    while current_date <= end_date:
        count = Risk.objects.filter(created_at__date=current_date).count()
        risk_trend_data.append({
            'date': current_date.strftime('%Y-%m-%d'),
            'count': count
        })
        current_date += timedelta(days=1)
    
    # Policy trend analysis
    policy_trend_data = []
    current_date = start_date
    while current_date <= end_date:
        count = Policy.objects.filter(created_at__date=current_date).count()
        policy_trend_data.append({
            'date': current_date.strftime('%Y-%m-%d'),
            'count': count
        })
        current_date += timedelta(days=1)
    
    # Risk categories distribution
    risk_categories = RiskCategory.objects.annotate(
        risk_count=Count('risks')
    ).filter(risk_count__gt=0)
    
    # Top risk owners
    top_risk_owners = User.objects.annotate(
        risk_count=Count('owned_risks')
    ).filter(risk_count__gt=0).order_by('-risk_count')[:5]
    
    # Compliance framework distribution
    framework_distribution = ComplianceFramework.objects.annotate(
        checklist_count=Count('requirements__checklists')
    ).filter(checklist_count__gt=0)
    
    # Overdue items
    overdue_checklists = ComplianceChecklist.objects.filter(
        due_date__lt=timezone.now().date(),
        status__in=['TODO', 'IN_PROGRESS']
    ).count()
    
    overdue_policies = Policy.objects.filter(
        updated_at__lt=timezone.now() - timedelta(days=365)
    ).count()
    
    context = {
        'risk_trend_data': risk_trend_data,
        'policy_trend_data': policy_trend_data,
        'risk_categories': risk_categories,
        'top_risk_owners': top_risk_owners,
        'framework_distribution': framework_distribution,
        'overdue_checklists': overdue_checklists,
        'overdue_policies': overdue_policies,
    }
    
    return render(request, 'dashboard/analytics.html', context)