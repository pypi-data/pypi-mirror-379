"""
Test cases for Admin login functionality
"""

from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from users.models import User

class AdminLoginTestCase(TestCase):
    def setUp(self):
        """Set up test environment"""
        self.client = Client()
        self.admin_user = User.objects.create_user(
            username='admin',
            email='admin@test.com',
            password='testpass123',
            role=User.Role.ADMIN
        )
        self.regular_user = User.objects.create_user(
            username='employee',
            email='employee@test.com',
            password='testpass123',
            role=User.Role.EMPLOYEE
        )
        self.admin_login_url = reverse('users:admin_login')
        self.admin_dashboard_url = reverse('users:admin_dashboard')

    def test_admin_login_page_loads(self):
        """Test that the admin login page loads successfully"""
        response = self.client.get(self.admin_login_url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Admin Login')
        self.assertContains(response, 'Email / Username')
        self.assertContains(response, 'Password')

    def test_admin_login_success(self):
        """Test successful admin login"""
        response = self.client.post(self.admin_login_url, {
            'username': 'admin',
            'password': 'testpass123'
        }, follow=True)
        
        # Should redirect to admin dashboard
        self.assertRedirects(response, self.admin_dashboard_url)
        self.assertContains(response, 'Admin Dashboard')
        
        # User should be authenticated
        self.assertTrue(response.context['user'].is_authenticated)
        self.assertEqual(response.context['user'].role, User.Role.ADMIN)

    def test_admin_login_invalid_credentials(self):
        """Test admin login with invalid credentials"""
        response = self.client.post(self.admin_login_url, {
            'username': 'admin',
            'password': 'wrongpassword'
        })
        
        # Should stay on login page with error
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Please check your username and password and try again')

    def test_non_admin_login_denied(self):
        """Test that non-admin users cannot login to admin portal"""
        response = self.client.post(self.admin_login_url, {
            'username': 'employee',
            'password': 'testpass123'
        })
        
        # Should stay on login page with error
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Only admin users can access this portal')

    def test_authenticated_admin_access_dashboard(self):
        """Test that authenticated admin can access dashboard"""
        self.client.login(username='admin', password='testpass123')
        response = self.client.get(self.admin_dashboard_url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Admin Dashboard')

    def test_authenticated_non_admin_denied_dashboard(self):
        """Test that authenticated non-admin cannot access dashboard"""
        self.client.login(username='employee', password='testpass123')
        response = self.client.get(self.admin_dashboard_url)
        # Should be redirected to login or show permission denied
        self.assertEqual(response.status_code, 302)  # Redirect to login

    def test_session_timeout_configuration(self):
        """Test that session timeout is configured"""
        from django.conf import settings
        # Check that session timeout is set to 30 minutes (1800 seconds)
        self.assertEqual(settings.SESSION_COOKIE_AGE, 1800)
        self.assertTrue(settings.SESSION_EXPIRE_AT_BROWSER_CLOSE)
        self.assertTrue(settings.SESSION_SAVE_EVERY_REQUEST)