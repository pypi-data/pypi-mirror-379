from django.db import models
from django.conf import settings
from django.utils import timezone
from governance.models import Policy
from risk.models import Risk
from users.models import User

class Workflow(models.Model):
    """
    Workflow definition for approval processes
    """
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name

class WorkflowStep(models.Model):
    """
    Individual steps in a workflow
    """
    workflow = models.ForeignKey(Workflow, on_delete=models.CASCADE, related_name='steps')
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    order = models.PositiveIntegerField()
    approver_role = models.CharField(
        max_length=20,
        choices=User.Role.choices
    )
    required = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return f"{self.workflow.name} - Step {self.order}: {self.name}"

class PolicyApproval(models.Model):
    """
    Approval workflow for policies
    """
    class Status(models.TextChoices):
        PENDING = 'PENDING', 'Pending'
        APPROVED = 'APPROVED', 'Approved'
        REJECTED = 'REJECTED', 'Rejected'
        CANCELLED = 'CANCELLED', 'Cancelled'
    
    policy = models.ForeignKey(Policy, on_delete=models.CASCADE, related_name='approvals')
    workflow = models.ForeignKey(Workflow, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.PENDING)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Approval for {self.policy.title}"

class PolicyApprovalStep(models.Model):
    """
    Individual approval steps for a policy
    """
    class Status(models.TextChoices):
        PENDING = 'PENDING', 'Pending'
        APPROVED = 'APPROVED', 'Approved'
        REJECTED = 'REJECTED', 'Rejected'
    
    approval = models.ForeignKey(PolicyApproval, on_delete=models.CASCADE, related_name='steps')
    step = models.ForeignKey(WorkflowStep, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.PENDING)
    approver = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        related_name='policy_approvals'
    )
    comments = models.TextField(blank=True)
    approved_at = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return f"Step {self.step.order}: {self.step.name} - {self.status}"

class RiskApproval(models.Model):
    """
    Approval workflow for risks
    """
    class Status(models.TextChoices):
        PENDING = 'PENDING', 'Pending'
        APPROVED = 'APPROVED', 'Approved'
        REJECTED = 'REJECTED', 'Rejected'
        CANCELLED = 'CANCELLED', 'Cancelled'
    
    risk = models.ForeignKey(Risk, on_delete=models.CASCADE, related_name='approvals')
    workflow = models.ForeignKey(Workflow, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.PENDING)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Approval for {self.risk.title}"

class RiskApprovalStep(models.Model):
    """
    Individual approval steps for a risk
    """
    class Status(models.TextChoices):
        PENDING = 'PENDING', 'Pending'
        APPROVED = 'APPROVED', 'Approved'
        REJECTED = 'REJECTED', 'Rejected'
    
    approval = models.ForeignKey(RiskApproval, on_delete=models.CASCADE, related_name='steps')
    step = models.ForeignKey(WorkflowStep, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.PENDING)
    approver = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        related_name='risk_approvals'
    )
    comments = models.TextField(blank=True)
    approved_at = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return f"Step {self.step.order}: {self.step.name} - {self.status}"

class Comment(models.Model):
    """
    Comments on policies, risks, or compliance items
    """
    class ContentType(models.TextChoices):
        POLICY = 'POLICY', 'Policy'
        RISK = 'RISK', 'Risk'
        COMPLIANCE = 'COMPLIANCE', 'Compliance'
    
    content_type = models.CharField(max_length=20, choices=ContentType.choices)
    object_id = models.PositiveIntegerField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Comment by {self.author.username} on {self.content_type}"