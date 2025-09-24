from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.core.paginator import Paginator
from .models import AuditLog, TwoFactorAuth, LoginAttempt
from users.models import User
import pyotp
import qrcode
from io import BytesIO
import base64

@login_required
def audit_log_list(request):
    """
    Display list of audit logs
    """
    # Only admins can view audit logs
    if request.user.role != User.Role.ADMIN:
        messages.error(request, 'You do not have permission to view audit logs.')
        return redirect('dashboard:home')
    
    # Get all audit logs, ordered by timestamp
    audit_logs = AuditLog.objects.all().select_related('user')
    
    # Filter by user if specified
    user_filter = request.GET.get('user')
    if user_filter:
        audit_logs = audit_logs.filter(user__id=user_filter)
    
    # Filter by action if specified
    action_filter = request.GET.get('action')
    if action_filter:
        audit_logs = audit_logs.filter(action=action_filter)
    
    # Paginate results
    paginator = Paginator(audit_logs, 25)  # Show 25 logs per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    # Get distinct users for filter dropdown
    users = User.objects.all()
    
    return render(request, 'security/audit_log_list.html', {
        'page_obj': page_obj,
        'users': users,
        'user_filter': user_filter,
        'action_filter': action_filter,
    })

@login_required
def two_factor_setup(request):
    """
    Setup two-factor authentication for a user
    """
    # Check if 2FA already exists for this user
    two_factor, created = TwoFactorAuth.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        # Verify the 2FA code
        token = request.POST.get('token')
        totp = pyotp.TOTP(two_factor.secret_key)
        
        if totp.verify(token):
            two_factor.is_verified = True
            two_factor.enabled = True
            two_factor.save()
            
            # Generate backup codes
            backup_codes = two_factor.generate_backup_codes()
            two_factor.backup_codes = ','.join(backup_codes)
            two_factor.save()
            
            messages.success(request, 'Two-factor authentication has been enabled successfully.')
            return redirect('security:two_factor_backup_codes')
        else:
            messages.error(request, 'Invalid token. Please try again.')
    
    # Generate QR code for authenticator app
    if not two_factor.secret_key:
        import secrets
        two_factor.secret_key = pyotp.random_base32()
        two_factor.save()
    
    # Generate provisioning URI
    totp = pyotp.TOTP(two_factor.secret_key)
    provisioning_uri = totp.provisioning_uri(
        name=request.user.email,
        issuer_name="CompliEdge"
    )
    
    # Generate QR code
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(provisioning_uri)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    qr_code = base64.b64encode(buffer.getvalue()).decode()
    
    return render(request, 'security/two_factor_setup.html', {
        'qr_code': qr_code,
        'secret_key': two_factor.secret_key,
    })

@login_required
def two_factor_backup_codes(request):
    """
    Display backup codes for 2FA
    """
    two_factor = get_object_or_404(TwoFactorAuth, user=request.user)
    
    if not two_factor.enabled:
        messages.error(request, 'Two-factor authentication is not enabled.')
        return redirect('security:two_factor_setup')
    
    # Split backup codes
    backup_codes = two_factor.backup_codes.split(',') if two_factor.backup_codes else []
    
    return render(request, 'security/two_factor_backup_codes.html', {
        'backup_codes': backup_codes,
    })

@login_required
def two_factor_disable(request):
    """
    Disable two-factor authentication
    """
    if request.method == 'POST':
        two_factor = get_object_or_404(TwoFactorAuth, user=request.user)
        two_factor.enabled = False
        two_factor.is_verified = False
        two_factor.secret_key = ''
        two_factor.backup_codes = ''
        two_factor.save()
        
        messages.success(request, 'Two-factor authentication has been disabled.')
        return redirect('users:profile')
    
    return render(request, 'security/two_factor_disable.html')