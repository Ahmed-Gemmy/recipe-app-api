from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successfully(self):
        """Test creating a new user with an email is successful"""
        email = 'test@example.com'
        password = 'Testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normarlized(self):
        """Test the email for a new user is normalized"""
        email = 'test@EXAMPLE.COM'
        user =  get_user_model().objects.create_user(email, '123123')
        self.assertEqual(user.email, email.lower())