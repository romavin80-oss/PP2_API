from rest_framework.test import APITestCase, APIClient
from rest_framework import status

from .utils import get_member_user, get_test_test


class TestModelTestCase(APITestCase):
    def setUp(self):
        self.client: APIClient = self.client
        self.user = get_member_user()

        response = self.client.post('/users/token/', {'email': self.user.email, 'password': 'qwerty'})
        self.access_token = response.json().get('access')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

        self.test_object = get_test_test()

    def test_19_test_list(self):
        response = self.client.get('/test/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        if 'results' in response.json():
            self.assertEqual(response.json()['results'][0]['title'], "Финал по зоологии")
        else:
            self.assertEqual(response.json()[0]['title'], "Финал по зоологии")

    def test_20_test_detail_with_questions(self):
        response = self.client.get(f'/test/{self.test_object.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json().get('title'), "Финал по зоологии")

        self.assertIn('questions', response.json())
        self.assertTrue(len(response.json()['questions']) > 0)
