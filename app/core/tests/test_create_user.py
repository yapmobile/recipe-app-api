from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models


def sample_user(email='sampleuser@sample.com', password='samplepassword'):
    """Create a sample user"""
    return get_user_model().objects.create_user(email, password)


class ModelTests(TestCase):

    def test_create_user_with_email_password(self):
        """Test creating user with email and password"""

        email = 'someone@company.com'
        password = 'secretpassword'

        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalize(self):
        """Test the email of a new user is normailized"""
        email = 'someone@COMPANY.COM'

        user = get_user_model().objects.create_user(email=email, password='abc')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating a new user with invalid email address"""

        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, "abc")

    def test_create_new_superuser(self):
        """Test creating new super user"""

        superuser = get_user_model().objects.create_superuser(
            'superuer@company.com',
            'supersecret'
        )

        self.assertTrue(superuser.is_staff)
        self.assertTrue(superuser.is_superuser)

    def test_tag_str(self):
        """Test the tag string representation"""
        tag = models.Tag.objects.create(
            user=sample_user(),
            name='sampleTagName'
        )

        self.assertEqual(str(tag), tag.name)

    def test_ingredient_str(self):
        """Test the ingredient string representation"""
        ingredient = models.Ingredient.objects.create(
            user=sample_user(),
            name='cucumber'
        )

        self.assertEqual(str(ingredient), ingredient.name)
