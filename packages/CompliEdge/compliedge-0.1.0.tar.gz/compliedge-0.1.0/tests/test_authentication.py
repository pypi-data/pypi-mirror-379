"""
Authentication and Access Control Tests for CompliEdge GRC System
"""

from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse
from users.models import Company

User = get_user_model()

class AuthenticationTest(TestCase):
    def setUp(self):
        """Set up test environment"""
        self.client = Client()
        
        # Create a test company
        self.company = Company.objects.create(
            company_name="Test Company",
            company_code="TEST001"
        )
        
        # Create test users
        self.admin_user = User.objects.create_user(
            username='adminuser',
            email='admin@test.com',
            password='testpass123',
            role=User.Role.ADMIN,
            company=self.company
        )
        
        self.employee_user = User.objects.create_user(
            username='employeeuser',
            email='employee@test.com',
            password='testpass123',
            role=User.Role.EMPLOYEE,
            company=self.company
        )

    def test_login_page_loads(self):
        """Test that the login page loads correctly"""
        response = self.client.get(reverse('users:login'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Sign in to your account")

    def test_registration_page_loads(self):
        """Test that the registration page loads correctly"""
        response = self.client.get(reverse('users:register'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Create your account")

    def test_valid_login(self):
        """Test successful login"""
        response = self.client.post(reverse('users:login'), {
            'username': 'employeeuser',
            'password': 'testpass123'
        })
        # Should redirect to dashboard
        self.assertRedirects(response, reverse('dashboard:home'))

    def test_invalid_login(self):
        """Test login with invalid credentials"""
        response = self.client.post(reverse('users:login'), {
            'username': 'employeeuser',
            'password': 'wrongpassword'
        })
        # Should stay on login page with error message
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Invalid credentials")

    def test_authenticated_user_access_dashboard(self):
        """Test that authenticated users can access the dashboard"""
        self.client.login(username='employeeuser', password='testpass123')
        response = self.client.get(reverse('dashboard:home'))
        self.assertEqual(response.status_code, 200)

    def test_unauthenticated_user_redirect_dashboard(self):
        """Test that unauthenticated users are redirected from dashboard"""
        response = self.client.get(reverse('dashboard:home'))
        # Should redirect to login page
        self.assertRedirects(response, f"{reverse('users:login')}?next={reverse('dashboard:home')}")

    def test_logout_functionality(self):
        """Test logout functionality"""
        self.client.login(username='employeeuser', password='testpass123')
        response = self.client.get(reverse('users:logout'))
        # Should redirect to login page
        self.assertRedirects(response, reverse('users:login'))

    def test_company_code_required_registration(self):
        """Test that company code is required during registration"""
        response = self.client.post(reverse('users:register'), {
            'username': 'newuser',
            'first_name': 'New',
            'last_name': 'User',
            'email': 'new@test.com',
            'company_code': '',  # Empty company code
            'password1': 'complexpass123',
            'password2': 'complexpass123',
            'terms': True
        })
        # Should stay on registration page with error
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "This field is required.")

    def test_valid_company_code_registration(self):
        """Test registration with valid company code"""
        response = self.client.post(reverse('users:register'), {
            'username': 'newuser',
            'first_name': 'New',
            'last_name': 'User',
            'email': 'new@test.com',
            'company_code': 'TEST001',  # Valid company code
            'password1': 'complexpass123',
            'password2': 'complexpass123',
            'terms': True
        })
        # Should redirect to dashboard after successful registration
        self.assertRedirects(response, reverse('dashboard:home'))