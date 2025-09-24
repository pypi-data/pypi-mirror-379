from django.db import models
from django.conf import settings
from django.utils import timezone

class ComplianceFramework(models.Model):
    """
    Compliance frameworks like ISO, GDPR, etc.
    """
    name = models.CharField(max_length=100)
    description = models.TextField()
    abbreviation = models.CharField(max_length=20)
    
    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return f"{self.name} ({self.abbreviation})"

class ComplianceRequirement(models.Model):
    """
    Individual requirements within a compliance framework
    """
    framework = models.ForeignKey(ComplianceFramework, on_delete=models.CASCADE, related_name='requirements')
    clause = models.CharField(max_length=50)
    title = models.CharField(max_length=200)
    description = models.TextField()
    
    class Meta:
        ordering = ['framework', 'clause']
    
    def __str__(self):
        return f"{self.framework.abbreviation} {self.clause}: {self.title}"

class ComplianceChecklist(models.Model):
    """
    Checklist for tracking compliance requirements
    """
    class Status(models.TextChoices):
        TODO = 'TODO', 'To Do'
        IN_PROGRESS = 'IN_PROGRESS', 'In Progress'
        COMPLETED = 'COMPLETED', 'Completed'
        NOT_APPLICABLE = 'NOT_APPLICABLE', 'Not Applicable'
    
    requirement = models.ForeignKey(ComplianceRequirement, on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.TODO)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    due_date = models.DateField(null=True, blank=True)
    
    class Meta:
        ordering = ['requirement__framework', 'requirement__clause']
    
    def __str__(self):
        return f"{self.requirement}: {self.status}"

class ComplianceAudit(models.Model):
    """
    Audit records for compliance checks
    """
    framework = models.ForeignKey(ComplianceFramework, on_delete=models.CASCADE)
    auditor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    audit_date = models.DateField()
    findings = models.TextField()
    recommendations = models.TextField()
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    
    class Meta:
        ordering = ['-audit_date']
    
    def __str__(self):
        return f"Audit of {self.framework.name} on {self.audit_date}"