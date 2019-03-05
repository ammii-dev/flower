from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from core.models import Escort

from escort.serializers import EscortsSerializer


ESCORTS_URL = reverse('posts:escort-list')
CREATE_ESCORTS_URL = reverse('escort:escort-list')


class PublicEscortsApiTests(TestCase):
    """Test the publicly available Escort API"""

    def setUp(self):
        self.client = APIClient()

    def test_login_not_required_for_public(self):
        """Test that login required for retrieving Escorts"""
        res = self.client.get(ESCORTS_URL)

        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_retrieve_tags(self):
        """Test retrieving Escort"""
        user = get_user_model().objects.create_user(
            'other@londonappdev.com',
            'testpass'
        )
        Escort.objects.create(user=user, name='Vegan')
        Escort.objects.create(user=user, name='Dessert')

        res = self.client.get(ESCORTS_URL)

        escorts = Escort.objects.all().order_by('-name')
        serializer = EscortsSerializer(escorts, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)


class PrivateEscortsApiTests(TestCase):
    """Test the authorized user Escorts API"""

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            'test@londonappdev.com',
            'password',
        )
        self.client = APIClient()
        self.client.force_authenticate(self.user)

    def test_create_escort_successful(self):
        """Test creating a new escort"""
        payload = {'name': 'Simple'}
        res = self.client.post(ESCORTS_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

    def test_create_escort_invalid(self):
        """Test creating a new tag with invalid payload"""
        payload = {'name': ''}
        res = self.client.post(ESCORTS_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
