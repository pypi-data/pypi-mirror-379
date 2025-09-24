from django.test import TestCase
from django.contrib.auth import get_user_model
from ..models import UserProfile

User = get_user_model()

class UserModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123',
            first_name='Test',
            last_name='User',
            phone='1234567890'
        )
    
    def test_user_creation(self):
        self.assertEqual(self.user.username, 'testuser')
        self.assertEqual(self.user.email, 'test@example.com')
        self.assertEqual(self.user.first_name, 'Test')
        self.assertEqual(self.user.last_name, 'User')
        self.assertEqual(self.user.phone, '1234567890')
        self.assertEqual(self.user.role, User.Role.EMPLOYEE)
        self.assertFalse(self.user.mfa_enabled)
    
    def test_user_profile_creation(self):
        profile = UserProfile.objects.create(
            user=self.user,
            bio='This is a test bio',
            location='Test Location'
        )
        self.assertEqual(profile.user, self.user)
        self.assertEqual(profile.bio, 'This is a test bio')
        self.assertEqual(profile.location, 'Test Location')
    
    def test_user_str_representation(self):
        self.assertEqual(str(self.user), 'testuser')