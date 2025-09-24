from django.test import TestCase
from django.contrib.auth import get_user_model
from permissions.utils import (
    can_manage_users, can_manage_policies, can_manage_compliance_frameworks,
    can_define_risks, can_approve_workflows, can_conduct_audits,
    can_submit_risk_observations, can_acknowledge_policies, get_user_permissions
)

User = get_user_model()

class UtilsTestCase(TestCase):
    def setUp(self):
        # Create users with different roles
        self.admin_user = User.objects.create_user(
            username='admin', 
            email='admin@test.com', 
            password='testpass123',
            role=User.Role.ADMIN
        )
        self.manager_user = User.objects.create_user(
            username='manager', 
            email='manager@test.com', 
            password='testpass123',
            role=User.Role.MANAGER
        )
        self.auditor_user = User.objects.create_user(
            username='auditor', 
            email='auditor@test.com', 
            password='testpass123',
            role=User.Role.AUDITOR
        )
        self.employee_user = User.objects.create_user(
            username='employee', 
            email='employee@test.com', 
            password='testpass123',
            role=User.Role.EMPLOYEE
        )

    def test_can_manage_users(self):
        """Test can_manage_users function"""
        self.assertTrue(can_manage_users(self.admin_user))
        self.assertFalse(can_manage_users(self.manager_user))
        self.assertFalse(can_manage_users(self.auditor_user))
        self.assertFalse(can_manage_users(self.employee_user))

    def test_can_manage_policies(self):
        """Test can_manage_policies function"""
        self.assertTrue(can_manage_policies(self.admin_user))
        self.assertTrue(can_manage_policies(self.manager_user))
        self.assertFalse(can_manage_policies(self.auditor_user))
        self.assertFalse(can_manage_policies(self.employee_user))

    def test_can_manage_compliance_frameworks(self):
        """Test can_manage_compliance_frameworks function"""
        self.assertTrue(can_manage_compliance_frameworks(self.admin_user))
        self.assertFalse(can_manage_compliance_frameworks(self.manager_user))
        self.assertFalse(can_manage_compliance_frameworks(self.auditor_user))
        self.assertFalse(can_manage_compliance_frameworks(self.employee_user))

    def test_can_define_risks(self):
        """Test can_define_risks function"""
        self.assertTrue(can_define_risks(self.admin_user))
        self.assertTrue(can_define_risks(self.manager_user))
        self.assertFalse(can_define_risks(self.auditor_user))
        self.assertFalse(can_define_risks(self.employee_user))

    def test_can_approve_workflows(self):
        """Test can_approve_workflows function"""
        self.assertTrue(can_approve_workflows(self.admin_user))
        self.assertFalse(can_approve_workflows(self.manager_user))
        self.assertFalse(can_approve_workflows(self.auditor_user))
        self.assertFalse(can_approve_workflows(self.employee_user))

    def test_can_conduct_audits(self):
        """Test can_conduct_audits function"""
        self.assertTrue(can_conduct_audits(self.admin_user))
        self.assertTrue(can_conduct_audits(self.manager_user))
        self.assertTrue(can_conduct_audits(self.auditor_user))
        self.assertFalse(can_conduct_audits(self.employee_user))

    def test_can_submit_risk_observations(self):
        """Test can_submit_risk_observations function"""
        self.assertTrue(can_submit_risk_observations(self.admin_user))
        self.assertTrue(can_submit_risk_observations(self.manager_user))
        self.assertFalse(can_submit_risk_observations(self.auditor_user))
        self.assertTrue(can_submit_risk_observations(self.employee_user))

    def test_can_acknowledge_policies(self):
        """Test can_acknowledge_policies function"""
        self.assertTrue(can_acknowledge_policies(self.admin_user))
        self.assertTrue(can_acknowledge_policies(self.manager_user))
        self.assertTrue(can_acknowledge_policies(self.auditor_user))
        self.assertTrue(can_acknowledge_policies(self.employee_user))

    def test_get_user_permissions(self):
        """Test get_user_permissions function"""
        # Test admin permissions
        admin_perms = get_user_permissions(self.admin_user)
        self.assertTrue(admin_perms['can_manage_users'])
        self.assertTrue(admin_perms['can_manage_policies'])
        self.assertTrue(admin_perms['can_manage_compliance_frameworks'])
        self.assertTrue(admin_perms['can_define_risks'])
        self.assertTrue(admin_perms['can_approve_workflows'])
        self.assertTrue(admin_perms['can_conduct_audits'])
        self.assertTrue(admin_perms['can_submit_risk_observations'])
        self.assertTrue(admin_perms['can_acknowledge_policies'])
        self.assertFalse(admin_perms['is_read_only'])
        
        # Test manager permissions
        manager_perms = get_user_permissions(self.manager_user)
        self.assertFalse(manager_perms['can_manage_users'])
        self.assertTrue(manager_perms['can_manage_policies'])
        self.assertFalse(manager_perms['can_manage_compliance_frameworks'])
        self.assertTrue(manager_perms['can_define_risks'])
        self.assertFalse(manager_perms['can_approve_workflows'])
        self.assertTrue(manager_perms['can_conduct_audits'])
        self.assertTrue(manager_perms['can_submit_risk_observations'])
        self.assertTrue(manager_perms['can_acknowledge_policies'])
        self.assertFalse(manager_perms['is_read_only'])
        
        # Test auditor permissions
        auditor_perms = get_user_permissions(self.auditor_user)
        self.assertFalse(auditor_perms['can_manage_users'])
        self.assertFalse(auditor_perms['can_manage_policies'])
        self.assertFalse(auditor_perms['can_manage_compliance_frameworks'])
        self.assertFalse(auditor_perms['can_define_risks'])
        self.assertFalse(auditor_perms['can_approve_workflows'])
        self.assertTrue(auditor_perms['can_conduct_audits'])
        self.assertFalse(auditor_perms['can_submit_risk_observations'])
        self.assertTrue(auditor_perms['can_acknowledge_policies'])
        self.assertTrue(auditor_perms['is_read_only'])
        
        # Test employee permissions
        employee_perms = get_user_permissions(self.employee_user)
        self.assertFalse(employee_perms['can_manage_users'])
        self.assertFalse(employee_perms['can_manage_policies'])
        self.assertFalse(employee_perms['can_manage_compliance_frameworks'])
        self.assertFalse(employee_perms['can_define_risks'])
        self.assertFalse(employee_perms['can_approve_workflows'])
        self.assertFalse(employee_perms['can_conduct_audits'])
        self.assertTrue(employee_perms['can_submit_risk_observations'])
        self.assertTrue(employee_perms['can_acknowledge_policies'])
        self.assertFalse(employee_perms['is_read_only'])