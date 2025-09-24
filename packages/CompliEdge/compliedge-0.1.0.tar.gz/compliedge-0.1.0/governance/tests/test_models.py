from django.test import TestCase
from django.contrib.auth import get_user_model
from ..models import Policy, PolicyDocument, PolicyComment

User = get_user_model()

class PolicyModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        self.policy = Policy.objects.create(
            title='Test Policy',
            description='This is a test policy',
            content='This is the content of the test policy',
            version='1.0',
            status=Policy.Status.DRAFT,
            created_by=self.user
        )
    
    def test_policy_creation(self):
        self.assertEqual(self.policy.title, 'Test Policy')
        self.assertEqual(self.policy.description, 'This is a test policy')
        self.assertEqual(self.policy.content, 'This is the content of the test policy')
        self.assertEqual(self.policy.version, '1.0')
        self.assertEqual(self.policy.status, Policy.Status.DRAFT)
        self.assertEqual(self.policy.created_by, self.user)
    
    def test_policy_str_representation(self):
        self.assertEqual(str(self.policy), 'Test Policy')
    
    def test_policy_document_creation(self):
        document = PolicyDocument.objects.create(
            policy=self.policy,
            file='test_file.pdf',
            name='Test Document'
        )
        self.assertEqual(document.policy, self.policy)
        self.assertEqual(document.name, 'Test Document')
    
    def test_policy_comment_creation(self):
        comment = PolicyComment.objects.create(
            policy=self.policy,
            author=self.user,
            content='This is a test comment'
        )
        self.assertEqual(comment.policy, self.policy)
        self.assertEqual(comment.author, self.user)
        self.assertEqual(comment.content, 'This is a test comment')