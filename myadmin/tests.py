from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .models import User

class UserModelTests(TestCase):
    def get_user_name(self):
        return User.objects.all()