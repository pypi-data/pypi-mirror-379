from django.test import TestCase, RequestFactory
from django.contrib.auth import get_user_model
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from permissions.decorators import (
    role_required, admin_required, manager_required, 
    auditor_required, employee_required
)

User = get_user_model()

# Simple view for testing
def test_view(request):
    return HttpResponse("Success")

class DecoratorTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
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

    def test_role_required_allows_correct_roles(self):
        """Test that role_required allows users with correct roles"""
        # Create a decorator that allows only ADMIN and MANAGER
        decorator = role_required([User.Role.ADMIN, User.Role.MANAGER])
        decorated_view = decorator(test_view)
        
        # Test with admin user
        request = self.factory.get('/')
        request.user = self.admin_user
        response = decorated_view(request)
        self.assertEqual(response.status_code, 200)
        
        # Test with manager user
        request.user = self.manager_user
        response = decorated_view(request)
        self.assertEqual(response.status_code, 200)

    def test_role_required_denies_incorrect_roles(self):
        """Test that role_required denies users with incorrect roles"""
        # Create a decorator that allows only ADMIN
        decorator = role_required([User.Role.ADMIN])
        decorated_view = decorator(test_view)
        
        # Test with manager user (should be denied)
        request = self.factory.get('/')
        request.user = self.manager_user
        
        with self.assertRaises(PermissionDenied):
            decorated_view(request)

    def test_admin_required(self):
        """Test admin_required decorator"""
        decorated_view = admin_required(test_view)
        
        # Test with admin user (should be allowed)
        request = self.factory.get('/')
        request.user = self.admin_user
        response = decorated_view(request)
        self.assertEqual(response.status_code, 200)
        
        # Test with manager user (should be denied)
        request.user = self.manager_user
        with self.assertRaises(PermissionDenied):
            decorated_view(request)

    def test_manager_required(self):
        """Test manager_required decorator"""
        decorated_view = manager_required(test_view)
        
        # Test with admin user (should be allowed)
        request = self.factory.get('/')
        request.user = self.admin_user
        response = decorated_view(request)
        self.assertEqual(response.status_code, 200)
        
        # Test with manager user (should be allowed)
        request.user = self.manager_user
        response = decorated_view(request)
        self.assertEqual(response.status_code, 200)
        
        # Test with auditor user (should be denied)
        request.user = self.auditor_user
        with self.assertRaises(PermissionDenied):
            decorated_view(request)

    def test_auditor_required(self):
        """Test auditor_required decorator"""
        decorated_view = auditor_required(test_view)
        
        # Test with admin user (should be allowed)
        request = self.factory.get('/')
        request.user = self.admin_user
        response = decorated_view(request)
        self.assertEqual(response.status_code, 200)
        
        # Test with manager user (should be allowed)
        request.user = self.manager_user
        response = decorated_view(request)
        self.assertEqual(response.status_code, 200)
        
        # Test with auditor user (should be allowed)
        request.user = self.auditor_user
        response = decorated_view(request)
        self.assertEqual(response.status_code, 200)
        
        # Test with employee user (should be denied)
        request.user = self.employee_user
        with self.assertRaises(PermissionDenied):
            decorated_view(request)

    def test_employee_required(self):
        """Test employee_required decorator"""
        decorated_view = employee_required(test_view)
        
        # Test with all roles (should be allowed)
        for user in [self.admin_user, self.manager_user, self.auditor_user, self.employee_user]:
            request = self.factory.get('/')
            request.user = user
            response = decorated_view(request)
            self.assertEqual(response.status_code, 200)