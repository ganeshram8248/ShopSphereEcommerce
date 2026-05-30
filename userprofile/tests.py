from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile

class ProfileTest(TestCase):

    def test_profile_created(self):
        user = User.objects.create_user(
            username="testuser",
            password="12345"
        )

        self.assertTrue(Profile.objects.filter(user=user).exists())