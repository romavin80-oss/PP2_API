from rest_framework.test import APITestCase
from rest_framework import status

from sections.test_sections.utils import get_member_user, get_test_question


class QuestionTestCase(APITestCase):
    def setUp(self):
        self.user = get_member_user()
        response = self.client.post('/users/token/', {'email': self.user.email, 'password': 'qwerty'})
        self.access_token = response.json().get('access')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        self.question = get_test_question()

    def test_16_question_list(self):
        response = self.client.get('/question/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['results'][0]['question'], "Test Question")

    def test_17_question_detail(self):
        response = self.client.get(f'/question/{self.question.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json().get('question'), "Test Question")

    def test_18_question_is_correct(self):
        correct_answer = {
            'member_answer': "Test Title Content",
        }
        wrong_answer = {
            'member_answer': "Wrong Title Content",
        }
        response = self.client.post(f'/question/{self.question.id}/', correct_answer)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json().get('is_correct'), True)
        response = self.client.post(f'/question/{self.question.id}/', wrong_answer)
        self.assertEqual(response.json().get('is_correct'), False)
