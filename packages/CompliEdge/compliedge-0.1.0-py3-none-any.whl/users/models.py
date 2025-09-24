from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.utils.crypto import get_random_string
from datetime import timedelta

class User(AbstractUser):
    """
    Custom user model for CompliEdge
    """
    class Role(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        MANAGER = "MANAGER", "Manager"
        EMPLOYEE = "EMPLOYEE", "Employee"
        AUDITOR = "AUDITOR", "Auditor"

    base_role = Role.EMPLOYEE

    role = models.CharField(
        max_length=50, 
        choices=Role.choices, 
        default=base_role
    )
    
    phone = models.CharField(max_length=15, blank=True)
    department = models.CharField(max_length=100, blank=True)
    position = models.CharField(max_length=100, blank=True)
    mfa_enabled = models.BooleanField(default=False)
    company = models.ForeignKey('Company', on_delete=models.SET_NULL, null=True, blank=True, related_name='employees')
    
    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = self.base_role
        return super().save(*args, **kwargs)

class Company(models.Model):
    """
    Company model for multi-tenant functionality
    """
    company_name = models.CharField(max_length=200, unique=True)
    company_code = models.CharField(max_length=50, unique=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='created_companies')
    created_at = models.DateTimeField(default=timezone.now)
    
    class Meta:
        verbose_name_plural = "Companies"
    
    def save(self, *args, **kwargs):
        if not self.company_code:
            # Generate a unique company code
            self.company_code = self.generate_unique_company_code()
        super().save(*args, **kwargs)
    
    def generate_unique_company_code(self):
        """Generate a unique company code"""
        while True:
            code = get_random_string(8, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
            if not Company.objects.filter(company_code=code).exists():
                return code
    
    def generate_invitation_link(self):
        """Generate a new invitation for this company"""
        invitation = Invitation.objects.create(company=self)
        return invitation.get_absolute_url()
    
    def __str__(self):
        return f"{self.company_name} ({self.company_code})"

class Invitation(models.Model):
    """Model for company invitations with expiration"""
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='invitations')
    token = models.CharField(max_length=50, unique=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    expires_at = models.DateTimeField()
    is_active = models.BooleanField(default=True)
    
    def save(self, *args, **kwargs):
        if not self.token:
            # Generate a unique token
            self.token = self.generate_unique_token()
        
        if not self.expires_at:
            # Set expiration to 7 days from now
            self.expires_at = timezone.now() + timedelta(days=7)
        
        super().save(*args, **kwargs)
    
    def generate_unique_token(self):
        """Generate a unique token"""
        while True:
            token = get_random_string(32, 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
            if not Invitation.objects.filter(token=token).exists():
                return token
    
    def is_valid(self):
        """Check if invitation is still valid"""
        return self.is_active and timezone.now() < self.expires_at
    
    def get_absolute_url(self):
        """Get the invitation URL"""
        from django.urls import reverse
        return reverse('users:accept_invitation', kwargs={'token': self.token})
    
    def __str__(self):
        return f"Invitation for {self.company.company_name} ({self.token})"

class UserProfile(models.Model):
    """
    Extended profile information for users
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    
    def __str__(self):
        return f"{self.user.username}'s Profile"


class Team(models.Model):
    """
    Team inside a Company with unique join code
    """
    company = models.ForeignKey('Company', on_delete=models.CASCADE, related_name='teams')
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    join_code = models.CharField(max_length=10, unique=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey('User', on_delete=models.SET_NULL, null=True, blank=True, related_name='created_teams')

    class Meta:
        unique_together = ('company', 'name')

    def save(self, *args, **kwargs):
        if not self.join_code:
            self.join_code = self.generate_unique_join_code()
        super().save(*args, **kwargs)

    def generate_unique_join_code(self):
        while True:
            code = get_random_string(6, 'ABCDEFGHJKLMNPQRSTUVWXYZ23456789')
            if not Team.objects.filter(join_code=code).exists():
                return code

    def __str__(self):
        return f"{self.name} - {self.company.company_name}"


class TeamMembership(models.Model):
    """Users membership in a team"""
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='team_memberships')
    team = models.ForeignKey('Team', on_delete=models.CASCADE, related_name='memberships')
    joined_at = models.DateTimeField(default=timezone.now)
    is_owner = models.BooleanField(default=False)

    class Meta:
        unique_together = ('user', 'team')

    def __str__(self):
        return f"{self.user.username} -> {self.team.name}"