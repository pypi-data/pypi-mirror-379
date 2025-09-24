from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse
from django.core.paginator import Paginator
from .models import Policy, PolicyDocument, PolicyComment
from .forms import PolicyForm, PolicyCommentForm
from permissions.decorators import admin_required, manager_required, auditor_required, employee_required
from permissions.utils import can_manage_policies
from users.models import User

@login_required
@auditor_required
def policy_list(request):
    """
    Display list of policies with filtering options
    """
    policies = Policy.objects.all()
    
    # Filter by status
    status_filter = request.GET.get('status')
    if status_filter:
        policies = policies.filter(status=status_filter)
    
    # Search
    search_query = request.GET.get('search')
    if search_query:
        policies = policies.filter(title__icontains=search_query)
    
    # Pagination
    paginator = Paginator(policies, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'governance/policy_list.html', {
        'page_obj': page_obj,
        'status_choices': Policy.Status.choices
    })

@login_required
@auditor_required
def policy_detail(request, pk):
    """
    Display policy details with comments
    """
    policy = get_object_or_404(Policy, pk=pk)
    comments = policy.comments.all().order_by('-created_at')
    
    if request.method == 'POST':
        # Only non-auditors can add comments
        if request.user.role != User.Role.AUDITOR:
            comment_form = PolicyCommentForm(request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.policy = policy
                comment.author = request.user
                comment.save()
                messages.success(request, 'Comment added successfully!')
                return redirect('governance:policy_detail', pk=policy.pk)
        else:
            messages.error(request, 'Auditors can only view policies.')
    
    comment_form = PolicyCommentForm()
    
    return render(request, 'governance/policy_detail.html', {
        'policy': policy,
        'comments': comments,
        'comment_form': comment_form,
        'can_manage_policies': can_manage_policies(request.user)
    })

@admin_required
def policy_create(request):
    """
    Create a new policy (Admin only)
    """
    if request.method == 'POST':
        form = PolicyForm(request.POST)
        if form.is_valid():
            policy = form.save(commit=False)
            policy.created_by = request.user
            policy.save()
            messages.success(request, 'Policy created successfully!')
            return redirect('governance:policy_detail', pk=policy.pk)
    else:
        form = PolicyForm()
    
    return render(request, 'governance/policy_form.html', {'form': form, 'title': 'Create Policy'})

@admin_required
def policy_edit(request, pk):
    """
    Edit an existing policy (Admin only)
    """
    policy = get_object_or_404(Policy, pk=pk)
    
    if request.method == 'POST':
        form = PolicyForm(request.POST, instance=policy)
        if form.is_valid():
            policy = form.save()
            messages.success(request, 'Policy updated successfully!')
            return redirect('governance:policy_detail', pk=policy.pk)
    else:
        form = PolicyForm(instance=policy)
    
    return render(request, 'governance/policy_form.html', {
        'form': form, 
        'policy': policy,
        'title': 'Edit Policy'
    })

@login_required
def policy_document_download(request, pk):
    """
    Download a policy document
    """
    document = get_object_or_404(PolicyDocument, pk=pk)
    response = HttpResponse(document.file, content_type='application/octet-stream')
    response['Content-Disposition'] = f'attachment; filename="{document.name}"'
    return response