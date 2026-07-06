from typing import cast
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status

from sections.test.utils import get_admin_user, get_test_section


class QuizTestsAdmin(APITestCase):
    def setUp(self):
        self.client = cast(APIClient, self.client)
        self.user = get_admin_user()

        # Получаем JWT-токен для авторизации
        response = self.client.post('/users/token/', {'email': self.user.email, 'password': 'qwerty'})
        self.access_token = response.json().get('access', '')
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)

        # Создаем тестовый раздел для привязки теста
        self.test_section = get_test_section()

    def test_08_quiz_create(self):
        data = {
            'section': self.test_section.id,
            'title': "Итоговый тест по разделу",
            'description': "Проверка знаний",
            'questions': []
        }

        # Автоматически собираем URL по имени маршрута 'sections:test_create'
        response = self.client.post(reverse('sections:test_create'), data=data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json().get('title'), "Итоговый тест по разделу")

    def test_09_quiz_list(self):
        response = self.client.get(reverse('sections:test_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
