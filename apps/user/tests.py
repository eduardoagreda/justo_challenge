from django.test import TestCase
from django.contrib.auth import get_user_model

class UsersManagersTests(TestCase):

    def test_create_assassin(self):
        User = get_user_model()
        assassin = User.objects.create_user(email='assassin@spycompany.com', password='assassins1')
        self.assertEqual(assassin.email, 'assassin@spycompany.com')
        self.assertTrue(assassin.is_active)
        self.assertFalse(assassin.is_staff)
        self.assertFalse(assassin.is_superuser)
        try:
            self.assertIsNone(assassin.username)
        except AttributeError:
            pass
        with self.assertRaises(TypeError):
            User.objects.create_user()
        with self.assertRaises(TypeError):
            User.objects.create_user(email='')
        with self.assertRaises(ValueError):
            User.objects.create_user(email='', password="assassins")

    def test_create_manager(self):
        User = get_user_model()
        manager_assassins = User.objects.create_superuser(email='manager@spycompany.com', password='manager1')
        self.assertEqual(manager_assassins.email, 'manager@spycompany.com')
        self.assertTrue(manager_assassins.is_active)
        self.assertTrue(manager_assassins.is_staff)
        self.assertFalse(manager_assassins.is_superuser)
        try:
            self.assertIsNone(manager_assassins.username)
        except AttributeError:
            pass
        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                email='', password='manager1', is_staff=False)

    def test_create_boss(self):
        User = get_user_model()
        the_boss_user = User.objects.create_superuser(email='the_boss@spycompany.com', password='theboss1')
        self.assertEqual(the_boss_user.email, 'the_boss@spycompany.com')
        self.assertTrue(the_boss_user.is_active)
        self.assertTrue(the_boss_user.is_staff)
        self.assertTrue(the_boss_user.is_superuser)
        try:
            self.assertIsNone(the_boss_user.username)
        except AttributeError:
            pass
        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                email='', password='theboss2', is_superuser=False)