from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib import messages
from django.utils import timezone
from .models import PolicyApproval, PolicyApprovalStep, RiskApproval, RiskApprovalStep, Comment
from governance.models import Policy
from risk.models import Risk
from users.models import User
from permissions.decorators import admin_required, manager_required

@login_required
def policy_approve(request, policy_id):
    """
    Start approval workflow for a policy
    """
    policy = get_object_or_404(Policy, id=policy_id)
    
    # Check if user has permission to initiate approval
    if request.user != policy.created_by and request.user.role not in [User.Role.ADMIN, User.Role.MANAGER]:
        messages.error(request, 'You do not have permission to initiate approval for this policy.')
        return redirect('governance:policy_detail', policy_id=policy.id)
    
    # Check if policy is already in approval
    if hasattr(policy, 'approval'):
        messages.info(request, 'This policy is already in the approval workflow.')
        return redirect('workflow:policy_approval_detail', policy_id=policy.id, approval_id=policy.approval.id)
    
    # Create approval workflow (simplified for now)
    approval = PolicyApproval.objects.create(
        policy=policy,
        workflow_id=1,  # Default workflow
        status=PolicyApproval.Status.PENDING
    )
    
    messages.success(request, 'Approval workflow initiated successfully.')
    return redirect('workflow:policy_approval_detail', policy_id=policy.id, approval_id=approval.id)

@login_required
def policy_approval_detail(request, policy_id, approval_id):
    """
    View approval workflow details for a policy
    """
    policy = get_object_or_404(Policy, id=policy_id)
    approval = get_object_or_404(PolicyApproval, id=approval_id, policy=policy)
    
    return render(request, 'workflow/policy_approval_detail.html', {
        'policy': policy,
        'approval': approval,
        'steps': approval.steps.all()
    })

@login_required
def risk_approve(request, risk_id):
    """
    Start approval workflow for a risk
    """
    risk = get_object_or_404(Risk, id=risk_id)
    
    # Check if user has permission to initiate approval
    if request.user != risk.identified_by and request.user.role not in [User.Role.ADMIN, User.Role.MANAGER]:
        messages.error(request, 'You do not have permission to initiate approval for this risk.')
        return redirect('risk:risk_detail', risk_id=risk.id)
    
    # Check if risk is already in approval
    if hasattr(risk, 'approval'):
        messages.info(request, 'This risk is already in the approval workflow.')
        return redirect('workflow:risk_approval_detail', risk_id=risk.id, approval_id=risk.approval.id)
    
    # Create approval workflow (simplified for now)
    approval = RiskApproval.objects.create(
        risk=risk,
        workflow_id=1,  # Default workflow
        status=RiskApproval.Status.PENDING
    )
    
    messages.success(request, 'Approval workflow initiated successfully.')
    return redirect('workflow:risk_approval_detail', risk_id=risk.id, approval_id=approval.id)

@login_required
def risk_approval_detail(request, risk_id, approval_id):
    """
    View approval workflow details for a risk
    """
    risk = get_object_or_404(Risk, id=risk_id)
    approval = get_object_or_404(RiskApproval, id=approval_id, risk=risk)
    
    return render(request, 'workflow/risk_approval_detail.html', {
        'risk': risk,
        'approval': approval,
        'steps': approval.steps.all()
    })

@login_required
def add_comment(request):
    """
    Add a comment to a policy, risk, or compliance item
    """
    if request.method == 'POST':
        content_type = request.POST.get('content_type')
        object_id = request.POST.get('object_id')
        content = request.POST.get('content')
        
        if content_type and object_id and content:
            Comment.objects.create(
                content_type=content_type,
                object_id=object_id,
                author=request.user,
                content=content
            )
            messages.success(request, 'Comment added successfully.')
        else:
            messages.error(request, 'Failed to add comment. Please provide all required information.')
    
    # Redirect back to the referring page
    return redirect(request.META.get('HTTP_REFERER', '/'))