from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.contrib.auth.models import User
from .models import UserProfile

class UserRegistrationTestCase(TestCase):
    def test_user_registration(self):
        response = self.client.post('/', {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password': 'password123',
            'user_type': 'normal_user'
        })
        self.assertEqual(response.status_code, 302)  # Redirects after success
        self.assertTrue(User.objects.filter(username='testuser').exists())
        self.assertTrue(UserProfile.objects.filter(user__username='testuser').exists())
