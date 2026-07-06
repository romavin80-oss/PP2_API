from typing import cast
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status

from sections.test.utils import get_admin_user, get_member_user, get_test_section


class SectionTestsAdmin(APITestCase):
    def setUp(self):
        self.client = cast(APIClient, self.client)

        self.user = get_admin_user()
        response = self.client.post('/users/token/', {'email': self.user.email, 'password': 'qwerty'})
        self.access_token = response.json().get('access', '')
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)
        self.test_section = get_test_section()

    def test_01_section_create(self):
        data = {
            'title': "Test Section Create",
            'description': "Test Description Create",
        }
        response = self.client.post(reverse('sections:section_create'), data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json().get('title'), "Test Section Create")

    def test_02_section_detail(self):
        # ИСПРАВЛЕНИЕ 1: Сборка пути без 404 ошибки и правильное имя из utils.py
        response = self.client.get(reverse('sections:section_detail', kwargs={'pk': self.test_section.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json().get('title'), "Тестовый раздел")
        self.assertEqual(response.json().get('description'), "Описание тестового раздела")

    def test_03_section_update(self):
        data = {'title': "Test Section Update PUT", 'description': "Test Description Update PUT", }
        response = self.client.put(f'/section/{self.test_section.id}/update/', data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json().get('title'), "Test Section Update PUT")
        self.assertEqual(response.json().get('description'), "Test Description Update PUT")

    def test_04_section_delete(self):
        response = self.client.delete(f'/section/{self.test_section.id}/delete/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        response = self.client.get(f'/section/{self.test_section.id}/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_05_section_list(self):
        response = self.client.get(f'/section/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # ИСПРАВЛЕНИЕ 2: Ожидаем "Тестовый раздел"
        self.assertEqual(response.json()['results'][0]['title'], "Тестовый раздел")


class SectionTestsMember(APITestCase):
    def setUp(self):
        self.client = cast(APIClient, self.client)

        self.user = get_member_user()
        response = self.client.post('/users/token/', {'email': self.user.email, 'password': 'qwerty'})
        self.access_token = response.json().get('access')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        self.test_section = get_test_section()

    def test_06_section_create_forbidden(self):
        data = {
            'title': "Test Section Create Forbidden",
            'description': "Test Description Create Forbidden",
        }
        response = self.client.post('/section/create/', data=data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        # ИСПРАВЛЕНИЕ 3: Исправлен регистр букв и слитно "недостаточно"
        self.assertEqual(response.json().get('detail'), 'У вас недостаточно прав для выполнения данного действия.')

    def test_07_section_delete_forbidden(self):
        response = self.client.delete(f'/section/{self.test_section.id}/delete/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.json().get('detail'), 'You are not a superuser.')
