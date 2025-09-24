from django.core.management.base import BaseCommand
from notifications.services import NotificationService

class Command(BaseCommand):
    help = 'Send smart notifications for compliance issues, risks, and approvals'

    def handle(self, *args, **options):
        self.stdout.write('Sending compliance notifications...')
        NotificationService.send_compliance_notifications()
        self.stdout.write(self.style.SUCCESS('Successfully sent compliance notifications'))

        self.stdout.write('Sending risk notifications...')
        NotificationService.send_risk_notifications()
        self.stdout.write(self.style.SUCCESS('Successfully sent risk notifications'))

        self.stdout.write('Sending approval notifications...')
        NotificationService.send_approval_notifications()
        self.stdout.write(self.style.SUCCESS('Successfully sent approval notifications'))

        self.stdout.write(self.style.SUCCESS('All notifications sent successfully!'))