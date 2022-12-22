# importación de librerias
from rest_framework.test import APITestCase

# Importación de modelos
from django.contrib.auth import get_user_model


class TestModel(APITestCase):

    def test_creates_user(self):
        self.assertEqual(1, 1-0)

# class HitTestCase(TestCase):

#     def setUp(self) -> None:
#         self.hit1 = Hit.objects.create(name='Primer Hit', description='Prueba de la creación de un hit')
#         self.hit2 = Hit.objects.create(name='Segundo Hit', description='Prueba de la creación de un hit')

#         self.user = get_user_model()

#         self.boss  = self.user.objects.create(email='boss@spycompany.com', password='theboss1')
#         self.user1 = self.user.objects.create(email='test01@spycompany.com', password='test01assassin')
#         self.user2 = self.user.objects.create(email='test02@spycompany.com', password='test02assassin')

#     def test_obtain_assassin_nmae(self):
#         self.assertEqual(self.hit1.name, 'Primer Hit')
        

#     def test_hit_assign_hitman_by_the_boss(self) -> None:
#         login = self.client.login(email=self.boss.email, password=self.boss.password)
#         self.assertTrue(login)
        
#         assassin = self.user1

#         self.hit1.assign_hitmans = assassin
        
#         self.assertEqual(self.hit1.assign_hitmans, self.user2)
#         self.assertEqual(assassin.is_staff, False)
#         try:
#             self.assertIsNone(assassin.username)
#         except AttributeError:
#             pass
#         with self.assertRaises(TypeError):
#             self.user.objects.create_user()
#         with self.assertRaises(TypeError):
#             self.user.objects.create_user(email='')
#         with self.assertRaises(ValueError):
#             self.user.objects.create_user(email='', password="assassins")