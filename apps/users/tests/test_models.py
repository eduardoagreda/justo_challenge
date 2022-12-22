# importación de librerias
from rest_framework.test import APITestCase

# Importación de modelos
from apps.users.models import CustomUser

class TestModel(APITestCase):

    def test_creates_user(self):
        user = CustomUser.objects.create_user(email='eduardo@gmail.com', password='eduardo021')
        self.assertIsInstance(user, CustomUser)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        self.assertEqual(user.email, 'eduardo@gmail.com')

    def test_raises_error_when_no_email(self):
        self.assertRaises(ValueError, CustomUser.objects.create_user, email='', password='eduardo021')

    def test_raises_error_whit_messages_when_no_email(self):
        with self.assertRaisesMessage(ValueError, 'El correo electrónico debe estar configurado'):
            CustomUser.objects.create_user(email='', password='eduardo123')

    def test_creates_superuser_whit_is_staff_status(self):
        with self.assertRaisesMessage(ValueError, 'Super usuario debe tener is_staff=True.'):
            CustomUser.objects.create_superuser(email='eduardo@gmail.com', password='eduardo021', is_staff=False)
    
    def test_creates_superuser_whit_is_superuser_status(self):
        with self.assertRaisesMessage(ValueError, 'Super usuario debe tener is_superuser=True.'):
            CustomUser.objects.create_superuser(email='eduardo@gmail.com', password='eduardo021', is_superuser=False)
    
    def test_creates_superuser(self):
        user = CustomUser.objects.create_superuser(email='eduardo@gmail.com', password='eduardo021')
        self.assertIsInstance(user, CustomUser)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
        self.assertEqual(user.email, 'eduardo@gmail.com')