from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):
    
    def test_create_user_with_email_sucessful(self):
        """Test creating a new user with an email in successful"""
        email = 'test@londonappdev.com'
        password = 'Testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
    
    def test_new_user_email_normalized(self):
        """ Test the email for a new user is normalized"""
        email = 'test@LALITKARKI.COM'
        user = get_user_model().objects.create_user(email, 'test123')

        self.assertEqual(user.email, email.lower())

    def test_create_new_superuser(self):
        """Test creating a new superuser """
        user = get_user_model().objects.create_super_user(
            'test@lalitkarki.com',
            'test123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)