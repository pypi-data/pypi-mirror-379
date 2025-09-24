from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.contrib.auth import get_user_model
from governance.models import Policy
from risk.models import Risk
from workflow.models import PolicyApproval, RiskApproval
from compliance.models import ComplianceChecklist

User = get_user_model()

def send_test_email(recipient_email, subject="Test Email from CompliEdge"):
    """
    Send a test email to verify email configuration
    """
    message = """
    This is a test email from CompliEdge.
    
    If you're receiving this, it means your email configuration is working correctly!
    
    Best regards,
    CompliEdge Team
    """
    
    try:
        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [recipient_email],
            fail_silently=False,
        )
        return True, "Test email sent successfully!"
    except Exception as e:
        return False, str(e)

def send_policy_approval_email(approval_id, recipient_email):
    """
    Send email notification for policy approval
    """
    try:
        approval = PolicyApproval.objects.select_related('policy', 'workflow').get(id=approval_id)
        subject = f"Policy Approval Required: {approval.policy.title}"
        
        html_message = render_to_string('notifications/policy_approval_email.html', {
            'approval': approval,
            'policy': approval.policy,
            'workflow': approval.workflow,
        })
        plain_message = strip_tags(html_message)
        
        send_mail(
            subject,
            plain_message,
            settings.DEFAULT_FROM_EMAIL,
            [recipient_email],
            html_message=html_message,
            fail_silently=False,
        )
        return True, "Policy approval email sent successfully!"
    except Exception as e:
        return False, str(e)

def send_risk_alert_email(risk_id, recipient_email):
    """
    Send email notification for high priority risk
    """
    try:
        risk = Risk.objects.select_related('category', 'owner').get(id=risk_id)
        subject = f"High Priority Risk Alert: {risk.title}"
        
        html_message = render_to_string('notifications/risk_alert_email.html', {
            'risk': risk,
            'category': risk.category,
            'owner': risk.owner,
        })
        plain_message = strip_tags(html_message)
        
        send_mail(
            subject,
            plain_message,
            settings.DEFAULT_FROM_EMAIL,
            [recipient_email],
            html_message=html_message,
            fail_silently=False,
        )
        return True, "Risk alert email sent successfully!"
    except Exception as e:
        return False, str(e)

def send_compliance_notification_email(checklist_id, recipient_email):
    """
    Send email notification for compliance item
    """
    try:
        checklist = ComplianceChecklist.objects.select_related('requirement', 'requirement__framework').get(id=checklist_id)
        subject = f"Compliance Notification: {checklist.requirement.title}"
        
        html_message = render_to_string('notifications/compliance_notification_email.html', {
            'checklist': checklist,
            'requirement': checklist.requirement,
            'framework': checklist.requirement.framework,
        })
        plain_message = strip_tags(html_message)
        
        send_mail(
            subject,
            plain_message,
            settings.DEFAULT_FROM_EMAIL,
            [recipient_email],
            html_message=html_message,
            fail_silently=False,
        )
        return True, "Compliance notification email sent successfully!"
    except Exception as e:
        return False, str(e)

def send_invitation_email(recipient_email, invite_link, role="Employee"):
    """
    Send invitation email with join link
    """
    subject = "You've been invited to join CompliEdge"
    
    html_message = render_to_string('notifications/invitation_email.html', {
        'invite_link': invite_link,
        'role': role,
    })
    plain_message = strip_tags(html_message)
    
    try:
        send_mail(
            subject,
            plain_message,
            settings.DEFAULT_FROM_EMAIL,
            [recipient_email],
            html_message=html_message,
            fail_silently=False,
        )
        return True, "Invitation email sent successfully!"
    except Exception as e:
        return False, str(e)