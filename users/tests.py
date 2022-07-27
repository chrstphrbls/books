# users/tests.py
from django.contrib.auth import get_user_model
from django.test import TestCase

class CustomUserTests(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='riri',
            email='riri@example.com',
            password='admin'
        )
        self.assertEqual(user.username,'riri')
        self.assertEqual(user.email,'riri@example.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        admin_user=User.objects.create_superuser(
            username ='admin',
            email='admin@example.com',
            password='admin'
        )
        self.assertEqual(admin_user.username,'admin')    
        self.assertEqual(admin_user.email,"admin@example.com")
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)


