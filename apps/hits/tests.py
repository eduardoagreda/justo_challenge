# importación de librerias
from django.test import TestCase

# Importación de modelos
from django.contrib.auth import get_user_model
from apps.hits.models import Hit


class HitTestCase(TestCase):

    def setUp(self) -> None:
        self.hit1 = Hit.objects.create(name='Primer Hit', description='Prueba de la creación de un hit')
        self.hit2 = Hit.objects.create(name='Segundo Hit', description='Prueba de la creación de un hit')

        self.user = get_user_model()

        self.user1 = self.user.objects.create(email='test01@spycompany.com', password='test01assassin')
        self.assertTrue(self.user1.is_active)
        self.assertFalse(self.user1.is_staff)
        self.assertFalse(self.user1.is_superuser)

    def test_hit_assign_hitman(self) -> None:
        assassin = self.user1
        self.hit1.assign_hitmans = assassin
        self.assertEqual(self.hit1.assign_hitmans, self.user1)
        self.assertEqual(assassin.is_staff, True)
        try:
            self.assertIsNone(assassin.username)
        except AttributeError:
            pass
        with self.assertRaises(TypeError):
            self.user.objects.create_user()
        with self.assertRaises(TypeError):
            self.user.objects.create_user(email='')
        with self.assertRaises(ValueError):
            self.user.objects.create_user(email='', password="assassins")