from django.core.management.base import BaseCommand
from notifications.email_utils import send_test_email

class Command(BaseCommand):
    help = 'Send a test email to verify email configuration'

    def add_arguments(self, parser):
        parser.add_argument('email', type=str, help='Recipient email address')
        parser.add_argument(
            '--subject',
            type=str,
            default='Test Email from CompliEdge',
            help='Email subject (default: "Test Email from CompliEdge")'
        )

    def handle(self, *args, **options):
        email = options['email']
        subject = options['subject']
        
        self.stdout.write(f'Sending test email to {email}...')
        
        success, message = send_test_email(email, subject)
        
        if success:
            self.stdout.write(
                self.style.SUCCESS(f'Successfully sent test email to {email}')
            )
        else:
            self.stdout.write(
                self.style.ERROR(f'Failed to send test email: {message}')
            )