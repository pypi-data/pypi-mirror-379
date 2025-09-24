from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from .models import Notification
from .email_utils import send_test_email
from django.contrib.auth import get_user_model

User = get_user_model()

@login_required
def notification_list(request):
    """
    Display list of user notifications
    """
    notifications = Notification.objects.filter(recipient=request.user).order_by('-created_at')
    return render(request, 'notifications/notification_list.html', {'notifications': notifications})

@require_http_methods(["POST"])
@login_required
def send_test_email_view(request):
    """
    View to send a test email (admin only)
    """
    if not request.user.is_staff:
        return JsonResponse({'success': False, 'error': 'Permission denied'})
    
    recipient_email = request.POST.get('email', '')
    if not recipient_email:
        return JsonResponse({'success': False, 'error': 'Email address is required'})
    
    success, message = send_test_email(recipient_email)
    
    if success:
        messages.success(request, f'Test email sent to {recipient_email}')
        return JsonResponse({'success': True, 'message': 'Test email sent successfully!'})
    else:
        messages.error(request, f'Failed to send test email: {message}')
        return JsonResponse({'success': False, 'error': message})