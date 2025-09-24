from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils import timezone
from .models import Notification, EmailNotification
from ai.compliance_checker import ComplianceChecker
from ai.risk_predictor import RiskPredictor

User = get_user_model()

class NotificationService:
    """
    Service for sending smart notifications
    """
    
    @staticmethod
    def send_in_app_notification(recipient, title, message, notification_type='INFO', priority='MEDIUM'):
        """
        Send in-app notification to a user
        """
        notification = Notification.objects.create(
            recipient=recipient,
            title=title,
            message=message,
            notification_type=notification_type,
            priority=priority
        )
        return notification
    
    @staticmethod
    def send_email_notification(recipient, subject, message):
        """
        Send email notification to a user
        """
        if recipient.email:
            try:
                send_mail(
                    subject,
                    message,
                    settings.DEFAULT_FROM_EMAIL,
                    [recipient.email],
                    fail_silently=False,
                )
                # Log the email notification
                EmailNotification.objects.create(
                    recipient=recipient,
                    subject=subject,
                    message=message,
                    is_sent=True,
                    sent_at_time=timezone.now()
                )
                return True
            except Exception as e:
                # Log the failed email notification
                EmailNotification.objects.create(
                    recipient=recipient,
                    subject=subject,
                    message=message,
                    is_sent=False
                )
                return False
        return False
    
    @staticmethod
    def send_compliance_notifications():
        """
        Send notifications for compliance issues
        """
        # Get compliance report
        report = ComplianceChecker.get_compliance_report()
        
        # Get users who should receive compliance notifications (Admins and Managers)
        recipients = User.objects.filter(role__in=[User.Role.ADMIN, User.Role.MANAGER])
        
        # Send notifications for overdue items
        if report['total_overdue_items'] > 0:
            title = f"Compliance Alert: {report['total_overdue_items']} Overdue Items"
            message = f"There are {report['total_overdue_items']} compliance items that are overdue. Please review the compliance report for details."
            
            for recipient in recipients:
                # Send in-app notification
                NotificationService.send_in_app_notification(
                    recipient,
                    title,
                    message,
                    notification_type='WARNING',
                    priority='HIGH'
                )
                
                # Send email notification
                NotificationService.send_email_notification(
                    recipient,
                    title,
                    f"Dear {recipient.get_full_name() or recipient.username},\n\n{message}\n\nPlease log in to CompliEdge to view the full compliance report.\n\nBest regards,\nCompliEdge Team"
                )
    
    @staticmethod
    def send_risk_notifications():
        """
        Send notifications for high-risk items
        """
        # Get risk predictions
        predictions = RiskPredictor.predict_risks()
        high_risk_predictions = [p for p in predictions if p['priority'] in ['HIGH', 'CRITICAL']]
        
        if high_risk_predictions:
            # Get users who should receive risk notifications (Admins, Managers, and Auditors)
            recipients = User.objects.filter(role__in=[User.Role.ADMIN, User.Role.MANAGER, User.Role.AUDITOR])
            
            title = f"Risk Alert: {len(high_risk_predictions)} High Priority Risks Identified"
            message = f"Our AI system has identified {len(high_risk_predictions)} high priority risks that require immediate attention."
            
            for recipient in recipients:
                # Send in-app notification
                NotificationService.send_in_app_notification(
                    recipient,
                    title,
                    message,
                    notification_type='WARNING',
                    priority='HIGH'
                )
                
                # Send email notification
                NotificationService.send_email_notification(
                    recipient,
                    title,
                    f"Dear {recipient.get_full_name() or recipient.username},\n\n{message}\n\nPlease log in to CompliEdge to view the full risk predictions.\n\nBest regards,\nCompliEdge Team"
                )
    
    @staticmethod
    def send_approval_notifications():
        """
        Send notifications for pending approvals
        """
        # This would check for pending approvals in the system
        # For now, we'll just send a general notification to admins if needed
        pending_approvals = 0  # In a real implementation, this would be calculated
        
        if pending_approvals > 0:
            recipients = User.objects.filter(role=User.Role.ADMIN)
            
            title = f"Approval Required: {pending_approvals} Pending Items"
            message = f"There are {pending_approvals} items pending your approval."
            
            for recipient in recipients:
                # Send in-app notification
                NotificationService.send_in_app_notification(
                    recipient,
                    title,
                    message,
                    notification_type='INFO',
                    priority='MEDIUM'
                )
                
                # Send email notification
                NotificationService.send_email_notification(
                    recipient,
                    title,
                    f"Dear {recipient.get_full_name() or recipient.username},\n\n{message}\n\nPlease log in to CompliEdge to review pending approvals.\n\nBest regards,\nCompliEdge Team"
                )