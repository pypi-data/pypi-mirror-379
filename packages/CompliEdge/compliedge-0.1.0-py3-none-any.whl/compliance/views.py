from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from .models import ComplianceFramework, ComplianceRequirement, ComplianceChecklist, ComplianceAudit
from .forms import ComplianceChecklistForm, ComplianceAuditForm
from permissions.decorators import admin_required, manager_required, auditor_required, employee_required
from permissions.utils import can_manage_compliance_frameworks, can_conduct_audits

@login_required
@auditor_required
def framework_list(request):
    """
    Display list of compliance frameworks
    """
    frameworks = ComplianceFramework.objects.all()
    
    # Search
    search_query = request.GET.get('search')
    if search_query:
        frameworks = frameworks.filter(name__icontains=search_query)
    
    return render(request, 'compliance/framework_list.html', {'frameworks': frameworks})

@login_required
@auditor_required
def framework_detail(request, pk):
    """
    Display framework details with requirements
    """
    framework = get_object_or_404(ComplianceFramework, pk=pk)
    requirements = framework.requirements.all()
    
    # Filter requirements
    clause_filter = request.GET.get('clause')
    if clause_filter:
        requirements = requirements.filter(clause__icontains=clause_filter)
    
    return render(request, 'compliance/framework_detail.html', {
        'framework': framework,
        'requirements': requirements,
        'can_manage_frameworks': can_manage_compliance_frameworks(request.user)
    })

@login_required
@auditor_required
def checklist_list(request):
    """
    Display compliance checklists with filtering options
    """
    checklists = ComplianceChecklist.objects.all()
    
    # Filter by framework
    framework_filter = request.GET.get('framework')
    if framework_filter:
        checklists = checklists.filter(requirement__framework_id=framework_filter)
    
    # Filter by status
    status_filter = request.GET.get('status')
    if status_filter:
        checklists = checklists.filter(status=status_filter)
    
    # Filter by assigned user
    assigned_filter = request.GET.get('assigned_to')
    if assigned_filter:
        checklists = checklists.filter(assigned_to_id=assigned_filter)
    
    # Pagination
    paginator = Paginator(checklists, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    frameworks = ComplianceFramework.objects.all()
    statuses = ComplianceChecklist.Status.choices
    
    return render(request, 'compliance/checklist_list.html', {
        'page_obj': page_obj,
        'frameworks': frameworks,
        'statuses': statuses,
        'can_conduct_audits': can_conduct_audits(request.user)
    })

@login_required
@manager_required
def checklist_update(request, pk):
    """
    Update a compliance checklist item (Manager and Admin)
    """
    checklist = get_object_or_404(ComplianceChecklist, pk=pk)
    
    if request.method == 'POST':
        form = ComplianceChecklistForm(request.POST, instance=checklist)
        if form.is_valid():
            form.save()
            messages.success(request, 'Checklist item updated successfully!')
            return redirect('compliance:checklist_list')
    else:
        form = ComplianceChecklistForm(instance=checklist)
    
    return render(request, 'compliance/checklist_form.html', {
        'form': form,
        'checklist': checklist
    })

@login_required
@auditor_required
def audit_list(request):
    """
    Display list of compliance audits
    """
    audits = ComplianceAudit.objects.all()
    
    # Filter by framework
    framework_filter = request.GET.get('framework')
    if framework_filter:
        audits = audits.filter(framework_id=framework_filter)
    
    # Filter by completion status
    completed_filter = request.GET.get('completed')
    if completed_filter:
        audits = audits.filter(completed=(completed_filter == 'true'))
    
    # Pagination
    paginator = Paginator(audits, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    frameworks = ComplianceFramework.objects.all()
    
    return render(request, 'compliance/audit_list.html', {
        'page_obj': page_obj,
        'frameworks': frameworks,
        'can_conduct_audits': can_conduct_audits(request.user)
    })

@admin_required
def audit_create(request):
    """
    Create a new compliance audit (Admin only)
    """
    if request.method == 'POST':
        form = ComplianceAuditForm(request.POST)
        if form.is_valid():
            audit = form.save(commit=False)
            audit.auditor = request.user
            audit.save()
            messages.success(request, 'Audit created successfully!')
            return redirect('compliance:audit_list')
    else:
        form = ComplianceAuditForm()
    
    return render(request, 'compliance/audit_form.html', {'form': form, 'title': 'Create Audit'})

@login_required
@auditor_required
def audit_detail(request, pk):
    """
    Display audit details
    """
    audit = get_object_or_404(ComplianceAudit, pk=pk)
    
    return render(request, 'compliance/audit_detail.html', {
        'audit': audit,
        'can_conduct_audits': can_conduct_audits(request.user)
    })