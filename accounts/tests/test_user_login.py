from django.contrib.auth.hashers import make_password
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.exceptions import ErrorDetail
from rest_framework.test import APIClient

from .user_factory import UserFactory

class UserLoginViewTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.client = APIClient()
        cls.login_url = reverse("user-login")
        cls.user = UserFactory(password=make_password("testpassword"))
        cls.valid_credentials = {"username": cls.user.username, "password": "testpassword"}
        cls.invalid_with_username_credentials = {"username": "username", "password": "testpassword"}
        cls.empty_username_credentials = {"username": "", "password": "testpassword"}

    def test_successful_login_returns_access_token(self):
        response = self.client.post(self.login_url, self.valid_credentials, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)
        self.access_token = response.data['access']

    def test_unsuccessful_login_returns_unauthorized_request(self):
        response = self.client.post(self.login_url, self.invalid_with_username_credentials, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_empty_username_returns_bad_request_with_error_details(self):
        response = self.client.post(self.login_url, self.empty_username_credentials, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        expected_error = {'username': [ErrorDetail(string='This field may not be blank.', code='blank')]}
        self.assertEqual(response.data, expected_error)
