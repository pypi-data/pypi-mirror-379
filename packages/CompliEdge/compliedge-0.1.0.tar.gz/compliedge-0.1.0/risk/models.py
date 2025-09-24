from django.db import models
from django.conf import settings
from django.utils import timezone

class RiskCategory(models.Model):
    """
    Categories for different types of risks
    """
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    
    class Meta:
        verbose_name_plural = "Risk Categories"
    
    def __str__(self):
        return self.name

class Risk(models.Model):
    """
    Model for risk identification and management
    """
    class Status(models.TextChoices):
        IDENTIFIED = 'IDENTIFIED', 'Identified'
        ASSESSED = 'ASSESSED', 'Assessed'
        MITIGATING = 'MITIGATING', 'Mitigating'
        MONITORING = 'MONITORING', 'Monitoring'
        CLOSED = 'CLOSED', 'Closed'
    
    class Priority(models.TextChoices):
        LOW = 'LOW', 'Low'
        MEDIUM = 'MEDIUM', 'Medium'
        HIGH = 'HIGH', 'High'
        CRITICAL = 'CRITICAL', 'Critical'
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey(RiskCategory, on_delete=models.CASCADE, related_name='risks')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='owned_risks')
    identified_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='identified_risks')
    
    # Risk assessment fields
    likelihood = models.IntegerField(help_text="Likelihood score (1-5)")
    impact = models.IntegerField(help_text="Impact score (1-5)")
    risk_score = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    priority = models.CharField(max_length=20, choices=Priority.choices, default=Priority.MEDIUM)
    
    # Mitigation fields
    mitigation_plan = models.TextField(blank=True)
    mitigation_owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='mitigation_risks')
    
    # Status tracking
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.IDENTIFIED)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    due_date = models.DateField(null=True, blank=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        # Calculate risk score (likelihood * impact)
        if self.likelihood and self.impact:
            self.risk_score = self.likelihood * self.impact
            
            # Set priority based on risk score
            score = self.likelihood * self.impact
            if score <= 5:
                self.priority = self.Priority.LOW
            elif score <= 10:
                self.priority = self.Priority.MEDIUM
            elif score <= 15:
                self.priority = self.Priority.HIGH
            else:
                self.priority = self.Priority.CRITICAL
        
        super().save(*args, **kwargs)

class RiskMitigation(models.Model):
    """
    Specific mitigation actions for risks
    """
    risk = models.ForeignKey(Risk, on_delete=models.CASCADE, related_name='mitigations')
    action = models.CharField(max_length=200)
    description = models.TextField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    due_date = models.DateField()
    completed = models.BooleanField(default=False)
    completion_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"Mitigation for {self.risk.title}: {self.action}"

class RiskReview(models.Model):
    """
    Periodic reviews of risks
    """
    risk = models.ForeignKey(Risk, on_delete=models.CASCADE, related_name='reviews')
    reviewer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    comments = models.TextField()
    review_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"Review of {self.risk.title} on {self.review_date.strftime('%Y-%m-%d')}"