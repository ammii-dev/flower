from django.test import TestCase
from django.contrib.auth import get_user_model
from core import models


def sample_user_escort(email='johnnii@gmail.com', password='emmy1234'):
    """ Create sample user """
    return get_user_model().objects.create_user(email, password)


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """test creating a new user with email"""
        email = "test@gmail.com"
        password = "test123"
        who = "escort"
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
            who=who
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
        self.assertEqual(user.who, who)

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized"""
        email = 'test@LONDONAPPDEV.com'
        user = get_user_model().objects.create_user(email, 'test123')
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            'test@londonappdev.com',
            'test123'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_escort_str(self):
        """Test the tag string representation"""
        escort = models.Escort.objects.create(
            user=sample_user_escort(),
            name='Jenny',

        )
        self.assertEqual(str(escort), escort.name)
