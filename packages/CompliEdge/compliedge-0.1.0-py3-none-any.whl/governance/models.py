from django.db import models
from django.conf import settings
from django.utils import timezone

class Policy(models.Model):
    """
    Model for governance policies
    """
    class Status(models.TextChoices):
        DRAFT = 'DRAFT', 'Draft'
        REVIEW = 'REVIEW', 'In Review'
        APPROVED = 'APPROVED', 'Approved'
        PUBLISHED = 'PUBLISHED', 'Published'
        ARCHIVED = 'ARCHIVED', 'Archived'

    title = models.CharField(max_length=200)
    description = models.TextField()
    content = models.TextField()
    version = models.CharField(max_length=20, default='1.0')
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.DRAFT)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='created_policies')
    approved_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='approved_policies')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    approved_at = models.DateTimeField(null=True, blank=True)
    published_at = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        verbose_name_plural = "Policies"
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if self.status == self.Status.APPROVED and not self.approved_at:
            self.approved_at = timezone.now()
        if self.status == self.Status.PUBLISHED and not self.published_at:
            self.published_at = timezone.now()
        super().save(*args, **kwargs)

class PolicyDocument(models.Model):
    """
    Supporting documents for policies
    """
    policy = models.ForeignKey(Policy, on_delete=models.CASCADE, related_name='documents')
    file = models.FileField(upload_to='policy_documents/')
    name = models.CharField(max_length=200)
    uploaded_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.name

class PolicyComment(models.Model):
    """
    Comments on policies
    """
    policy = models.ForeignKey(Policy, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Comment by {self.author.username} on {self.policy.title}"