from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.core.paginator import Paginator
from .models import Risk, RiskCategory, RiskMitigation, RiskReview
from .forms import RiskForm, RiskMitigationForm, RiskReviewForm
from permissions.decorators import admin_required, manager_required, auditor_required, employee_required
from permissions.utils import can_define_risks, can_conduct_audits, can_submit_risk_observations
from users.models import User

@login_required
@auditor_required
def risk_list(request):
    """
    Display list of risks with filtering options
    """
    risks = Risk.objects.all()
    
    # Filter by status
    status_filter = request.GET.get('status')
    if status_filter:
        risks = risks.filter(status=status_filter)
    
    # Filter by priority
    priority_filter = request.GET.get('priority')
    if priority_filter:
        risks = risks.filter(priority=priority_filter)
    
    # Filter by category
    category_filter = request.GET.get('category')
    if category_filter:
        risks = risks.filter(category_id=category_filter)
    
    # Search
    search_query = request.GET.get('search')
    if search_query:
        risks = risks.filter(title__icontains=search_query)
    
    # Pagination
    paginator = Paginator(risks, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    categories = RiskCategory.objects.all()
    
    return render(request, 'risk/risk_list.html', {
        'page_obj': page_obj,
        'status_choices': Risk.Status.choices,
        'priority_choices': Risk.Priority.choices,
        'categories': categories,
        'can_define_risks': can_define_risks(request.user),
        'can_conduct_audits': can_conduct_audits(request.user)
    })

@login_required
@auditor_required
def risk_detail(request, pk):
    """
    Display risk details with mitigations and reviews
    """
    risk = get_object_or_404(Risk, pk=pk)
    mitigations = risk.mitigations.all()
    reviews = risk.reviews.all().order_by('-review_date')
    
    return render(request, 'risk/risk_detail.html', {
        'risk': risk,
        'mitigations': mitigations,
        'reviews': reviews,
        'can_define_risks': can_define_risks(request.user),
        'can_conduct_audits': can_conduct_audits(request.user)
    })

@login_required
@manager_required
def risk_create(request):
    """
    Create a new risk (Manager and Admin)
    """
    if request.method == 'POST':
        form = RiskForm(request.POST)
        if form.is_valid():
            risk = form.save(commit=False)
            risk.identified_by = request.user
            risk.owner = request.user
            risk.save()
            messages.success(request, 'Risk created successfully!')
            return redirect('risk:risk_detail', pk=risk.pk)
    else:
        form = RiskForm()
    
    return render(request, 'risk/risk_form.html', {'form': form, 'title': 'Create Risk'})

@login_required
@manager_required
def risk_edit(request, pk):
    """
    Edit an existing risk (Manager and Admin)
    """
    risk = get_object_or_404(Risk, pk=pk)
    
    if request.method == 'POST':
        form = RiskForm(request.POST, instance=risk)
        if form.is_valid():
            risk = form.save()
            messages.success(request, 'Risk updated successfully!')
            return redirect('risk:risk_detail', pk=risk.pk)
    else:
        form = RiskForm(instance=risk)
    
    return render(request, 'risk/risk_form.html', {
        'form': form, 
        'risk': risk,
        'title': 'Edit Risk'
    })

@login_required
@manager_required
def mitigation_create(request, risk_pk):
    """
    Create a mitigation for a risk (Manager and Admin)
    """
    risk = get_object_or_404(Risk, pk=risk_pk)
    
    if request.method == 'POST':
        form = RiskMitigationForm(request.POST)
        if form.is_valid():
            mitigation = form.save(commit=False)
            mitigation.risk = risk
            mitigation.owner = request.user
            mitigation.save()
            messages.success(request, 'Mitigation created successfully!')
            return redirect('risk:risk_detail', pk=risk.pk)
    else:
        form = RiskMitigationForm()
    
    return render(request, 'risk/mitigation_form.html', {
        'form': form, 
        'risk': risk,
        'title': 'Create Mitigation'
    })

@login_required
@employee_required
def risk_predict(request):
    """
    AI-assisted risk prediction (simplified implementation)
    Available to all authenticated users
    """
    # This would be replaced with actual AI/ML logic in a real implementation
    # For now, we'll return an empty response
    return JsonResponse({'predictions': []})