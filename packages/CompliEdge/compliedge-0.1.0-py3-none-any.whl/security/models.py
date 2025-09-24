from django.db import models
from django.conf import settings
from django.utils import timezone

class AuditLog(models.Model):
    """
    Model for tracking user actions and system events
    """
    class Action(models.TextChoices):
        CREATE = 'CREATE', 'Create'
        READ = 'READ', 'Read'
        UPDATE = 'UPDATE', 'Update'
        DELETE = 'DELETE', 'Delete'
        LOGIN = 'LOGIN', 'Login'
        LOGOUT = 'LOGOUT', 'Logout'
        FAILED_LOGIN = 'FAILED_LOGIN', 'Failed Login'
        POLICY_APPROVAL = 'POLICY_APPROVAL', 'Policy Approval'
        RISK_ASSESSMENT = 'RISK_ASSESSMENT', 'Risk Assessment'
        COMPLIANCE_CHECK = 'COMPLIANCE_CHECK', 'Compliance Check'
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    action = models.CharField(max_length=20, choices=Action.choices)
    model_name = models.CharField(max_length=100, blank=True)
    object_id = models.PositiveIntegerField(null=True, blank=True)
    description = models.TextField(blank=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.TextField(blank=True)
    timestamp = models.DateTimeField(default=timezone.now)
    
    class Meta:
        ordering = ['-timestamp']
        indexes = [
            models.Index(fields=['user', '-timestamp']),
            models.Index(fields=['action', '-timestamp']),
        ]
    
    def __str__(self):
        if self.user:
            return f"{self.user.username} - {self.action} - {self.timestamp}"
        else:
            return f"System - {self.action} - {self.timestamp}"

class TwoFactorAuth(models.Model):
    """
    Model for storing 2FA information for users
    """
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='two_factor_auth')
    secret_key = models.CharField(max_length=100)
    backup_codes = models.TextField(blank=True)  # JSON formatted list of backup codes
    is_verified = models.BooleanField(default=False)
    enabled = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"2FA for {self.user.username}"
    
    def generate_backup_codes(self, count=10):
        """
        Generate backup codes for 2FA
        """
        import secrets
        codes = []
        for _ in range(count):
            code = ''.join(secrets.choice('0123456789') for _ in range(8))
            codes.append(code)
        return codes

class LoginAttempt(models.Model):
    """
    Model for tracking login attempts
    """
    username = models.CharField(max_length=150)
    ip_address = models.GenericIPAddressField()
    success = models.BooleanField(default=False)
    timestamp = models.DateTimeField(default=timezone.now)
    user_agent = models.TextField(blank=True)
    
    class Meta:
        ordering = ['-timestamp']
        indexes = [
            models.Index(fields=['username', '-timestamp']),
            models.Index(fields=['ip_address', '-timestamp']),
        ]
    
    def __str__(self):
        return f"Login attempt for {self.username} from {self.ip_address} - {'Success' if self.success else 'Failed'}"