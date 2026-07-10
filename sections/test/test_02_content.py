from rest_framework.test import APITestCase, APIClient
from rest_framework import status

from .utils import get_admin_user, get_member_user, get_test_content


class ContentTestAdmin(APITestCase):
    def setUp(self):
        self.client: APIClient = self.client

        self.user = get_admin_user()
        response = self.client.post('/users/token/', {'email': self.user.email, 'password': 'qwerty'})
        self.access_token = response.json().get('access')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        self.content = get_test_content()

    def test_08_content_create(self):
        data = {
            'section': self.content.section.id,
            'title': "Test content title create",
            'content': "Test content create",
        }

        response = self.client.post('/content/create/', data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json().get('title'), "Test content title create")
        self.assertEqual(response.json().get('content'), "Test content create")

    def test_09_content_detail(self):
        response = self.client.get(f'/content/{self.content.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json().get('title'), "Test Title Content")
        self.assertEqual(response.json().get('content'), "Test Content")

    def test_10_content_update(self):
        data = {
            'title': "Test content title PATCH",
        }
        response = self.client.patch(f'/content/{self.content.id}/update/', data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json().get('title'), "Test content title PATCH")

    def test_11_content_delete(self):
        response = self.client.delete(f'/content/{self.content.id}/delete/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        response = self.client.delete(f'/content/{self.content.id}/delete/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_12_content_list(self):
        response = self.client.get(f'/content/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['results'][0]['title'], "Test Title Content")


class ContentTestMember(APITestCase):
    def setUp(self):
        # Подсказка для PyCharm, чтобы убрать желтое предупреждение для credentials
        self.client: APIClient = self.client

        self.user = get_member_user()
        response = self.client.post('/users/token/', {'email': self.user.email, 'password': 'qwerty'})
        self.access_token = response.json().get('access')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        self.content = get_test_content()

    def test_13_content_create_forbidden(self):
        data = {
            'section': self.content.section.id,
            'title': "Test content title create FORBIDDEN",
            'content': "Test content create FORBIDDEN",
        }
        response = self.client.post('/content/create/', data=data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.json().get('detail'), "У вас недостаточно прав для выполнения данного действия.")

    def test_14_content_update_forbidden(self):
        data = {
            'title': "Test content title PATCH FORBIDDEN",
        }
        response = self.client.patch(f'/content/{self.content.id}/update/', data=data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.json().get('detail'), "У вас недостаточно прав для выполнения данного действия.")

    def test_15_content_delete_forbidden(self):
        response = self.client.delete(f'/content/{self.content.id}/delete/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.json().get('detail'), "You are not a superuser.")