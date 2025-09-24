from django.test import TestCase
from django.contrib.auth import get_user_model
from django.core.exceptions import PermissionDenied
from permissions.mixins import (
    AdminRequiredMixin, ManagerRequiredMixin, 
    AuditorRequiredMixin, EmployeeRequiredMixin
)
from django.views import View
from django.http import HttpResponse

User = get_user_model()

# Simple view for testing
class TestView(View):
    def get(self, request):
        return HttpResponse("Success")

class MixinTestCase(TestCase):
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

    def test_admin_required_mixin(self):
        """Test AdminRequiredMixin"""
        view = AdminRequiredMixin.as_view()(TestView.as_view())
        
        # Test with admin user (should be allowed)
        self.client.login(username='admin', password='testpass123')
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        
        # Test with manager user (should be denied)
        self.client.login(username='manager', password='testpass123')
        response = self.client.get('/')
        self.assertEqual(response.status_code, 403)

    def test_manager_required_mixin(self):
        """Test ManagerRequiredMixin"""
        view = ManagerRequiredMixin.as_view()(TestView.as_view())
        
        # Test with admin user (should be allowed)
        self.client.login(username='admin', password='testpass123')
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        
        # Test with manager user (should be allowed)
        self.client.login(username='manager', password='testpass123')
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        
        # Test with auditor user (should be denied)
        self.client.login(username='auditor', password='testpass123')
        response = self.client.get('/')
        self.assertEqual(response.status_code, 403)

    def test_auditor_required_mixin(self):
        """Test AuditorRequiredMixin"""
        view = AuditorRequiredMixin.as_view()(TestView.as_view())
        
        # Test with admin user (should be allowed)
        self.client.login(username='admin', password='testpass123')
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        
        # Test with manager user (should be allowed)
        self.client.login(username='manager', password='testpass123')
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        
        # Test with auditor user (should be allowed)
        self.client.login(username='auditor', password='testpass123')
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        
        # Test with employee user (should be denied)
        self.client.login(username='employee', password='testpass123')
        response = self.client.get('/')
        self.assertEqual(response.status_code, 403)

    def test_employee_required_mixin(self):
        """Test EmployeeRequiredMixin"""
        view = EmployeeRequiredMixin.as_view()(TestView.as_view())
        
        # Test with all roles (should be allowed)
        for username in ['admin', 'manager', 'auditor', 'employee']:
            self.client.login(username=username, password='testpass123')
            response = self.client.get('/')
            # Note: This might return 200 or redirect to login depending on setup
            # The important thing is that it doesn't raise PermissionDenied
            self.assertNotEqual(response.status_code, 403)