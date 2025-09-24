from datetime import datetime, timedelta
from django.utils import timezone
from governance.models import Policy
from compliance.models import ComplianceChecklist, ComplianceAudit

class ComplianceChecker:
    """
    Automated compliance checker that flags non-compliant policies or overdue tasks
    """
    
    @staticmethod
    def check_overdue_policies():
        """
        Check for policies that need to be reviewed or updated
        """
        # Get all policies
        policies = Policy.objects.all()
        overdue_policies = []
        
        for policy in policies:
            # Check if policy is overdue for review (older than 1 year)
            if policy.updated_at:
                days_since_update = (timezone.now() - policy.updated_at).days
                if days_since_update > 365:
                    overdue_policies.append({
                        'policy': policy,
                        'days_overdue': days_since_update - 365,
                        'severity': 'HIGH' if days_since_update > 730 else 'MEDIUM'
                    })
            
            # Check if draft policies have been pending too long
            if policy.status == 'DRAFT':
                days_in_draft = (timezone.now() - policy.created_at).days
                if days_in_draft > 30:
                    overdue_policies.append({
                        'policy': policy,
                        'days_overdue': days_in_draft - 30,
                        'severity': 'MEDIUM' if days_in_draft <= 90 else 'HIGH'
                    })
        
        return overdue_policies
    
    @staticmethod
    def check_overdue_checklists():
        """
        Check for compliance checklists that are overdue
        """
        # Get all checklists that are not completed and have due dates
        overdue_checklists = ComplianceChecklist.objects.exclude(
            status__in=['COMPLETED', 'NOT_APPLICABLE']
        ).filter(
            due_date__lt=timezone.now().date()
        )
        
        results = []
        for checklist in overdue_checklists:
            days_overdue = (timezone.now().date() - checklist.due_date).days
            results.append({
                'checklist': checklist,
                'days_overdue': days_overdue,
                'severity': 'HIGH' if days_overdue > 30 else 'MEDIUM'
            })
        
        return results
    
    @staticmethod
    def check_overdue_audits():
        """
        Check for audits that are overdue
        """
        # Get all audits that are not completed
        overdue_audits = ComplianceAudit.objects.filter(
            completed=False
        )
        
        results = []
        for audit in overdue_audits:
            # If audit has a scheduled date and it's past due
            if hasattr(audit, 'scheduled_date') and audit.scheduled_date and audit.scheduled_date < timezone.now().date():
                days_overdue = (timezone.now().date() - audit.scheduled_date).days
                results.append({
                    'audit': audit,
                    'days_overdue': days_overdue,
                    'severity': 'HIGH' if days_overdue > 30 else 'MEDIUM'
                })
            # If audit has no scheduled date but was created a long time ago
            elif (timezone.now() - audit.created_at).days > 90:
                days_overdue = (timezone.now() - audit.created_at).days - 90
                results.append({
                    'audit': audit,
                    'days_overdue': days_overdue,
                    'severity': 'MEDIUM'
                })
        
        return results
    
    @staticmethod
    def get_compliance_report():
        """
        Generate a comprehensive compliance report
        """
        overdue_policies = ComplianceChecker.check_overdue_policies()
        overdue_checklists = ComplianceChecker.check_overdue_checklists()
        overdue_audits = ComplianceChecker.check_overdue_audits()
        
        # Calculate compliance score
        total_items = len(overdue_policies) + len(overdue_checklists) + len(overdue_audits)
        if total_items == 0:
            compliance_score = 100
        else:
            # For simplicity, we'll calculate a basic score
            # In a real implementation, this would be more sophisticated
            compliance_score = max(0, 100 - (total_items * 5))
        
        return {
            'compliance_score': compliance_score,
            'overdue_policies': overdue_policies,
            'overdue_checklists': overdue_checklists,
            'overdue_audits': overdue_audits,
            'total_overdue_items': total_items
        }