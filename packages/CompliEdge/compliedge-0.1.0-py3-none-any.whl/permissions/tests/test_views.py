from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from governance.models import Policy
from risk.models import Risk, RiskCategory
from compliance.models import ComplianceFramework

User = get_user_model()

class ViewPermissionTestCase(TestCase):
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
        
        # Create test data
        self.policy = Policy.objects.create(
            title='Test Policy',
            description='Test Description',
            content='Test Content',
            created_by=self.admin_user
        )
        
        self.risk_category = RiskCategory.objects.create(
            name='Test Category',
            description='Test Description'
        )
        
        self.risk = Risk.objects.create(
            title='Test Risk',
            description='Test Description',
            category=self.risk_category,
            owner=self.admin_user,
            identified_by=self.admin_user
        )
        
        self.framework = ComplianceFramework.objects.create(
            name='Test Framework',
            description='Test Description'
        )

    def test_policy_create_view_permissions(self):
        """Test that only admin users can create policies"""
        url = reverse('governance:policy_create')
        
        # Test with admin user (should be allowed)
        self.client.login(username='admin', password='testpass123')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        
        # Test with manager user (should be denied)
        self.client.login(username='manager', password='testpass123')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 403)
        
        # Test with auditor user (should be denied)
        self.client.login(username='auditor', password='testpass123')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 403)
        
        # Test with employee user (should be denied)
        self.client.login(username='employee', password='testpass123')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 403)

    def test_risk_create_view_permissions(self):
        """Test that only admin and manager users can create risks"""
        url = reverse('risk:risk_create')
        
        # Test with admin user (should be allowed)
        self.client.login(username='admin', password='testpass123')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        
        # Test with manager user (should be allowed)
        self.client.login(username='manager', password='testpass123')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        
        # Test with auditor user (should be denied)
        self.client.login(username='auditor', password='testpass123')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 403)
        
        # Test with employee user (should be denied)
        self.client.login(username='employee', password='testpass123')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 403)

    def test_framework_create_view_permissions(self):
        """Test that only admin users can create compliance frameworks"""
        url = reverse('compliance:framework_create')
        
        # Test with admin user (should be allowed)
        self.client.login(username='admin', password='testpass123')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        
        # Test with manager user (should be denied)
        self.client.login(username='manager', password='testpass123')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 403)
        
        # Test with auditor user (should be denied)
        self.client.login(username='auditor', password='testpass123')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 403)
        
        # Test with employee user (should be denied)
        self.client.login(username='employee', password='testpass123')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 403)

    def test_policy_list_view_permissions(self):
        """Test that all authenticated users can view policy list"""
        url = reverse('governance:policy_list')
        
        # Test with all roles (should be allowed)
        for username in ['admin', 'manager', 'auditor', 'employee']:
            self.client.login(username=username, password='testpass123')
            response = self.client.get(url)
            self.assertEqual(response.status_code, 200)

    def test_risk_list_view_permissions(self):
        """Test that all authenticated users can view risk list"""
        url = reverse('risk:risk_list')
        
        # Test with all roles (should be allowed)
        for username in ['admin', 'manager', 'auditor', 'employee']:
            self.client.login(username=username, password='testpass123')
            response = self.client.get(url)
            self.assertEqual(response.status_code, 200)

    def test_framework_list_view_permissions(self):
        """Test that all authenticated users can view framework list"""
        url = reverse('compliance:framework_list')
        
        # Test with all roles (should be allowed)
        for username in ['admin', 'manager', 'auditor', 'employee']:
            self.client.login(username=username, password='testpass123')
            response = self.client.get(url)
            self.assertEqual(response.status_code, 200)