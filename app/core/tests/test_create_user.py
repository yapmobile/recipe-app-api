from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_password(self):
        """Test creating user with email and password"""

        email = "someone@company.com"
        password = "secretpassword"

        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalize(self):
        """Test the email of a new user is normailized"""
        email = "someone@COMPANY.COM"

        user = get_user_model().objects.create_user(email=email, password="abc")

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating a new user with invalid email address"""

        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, "abc")
