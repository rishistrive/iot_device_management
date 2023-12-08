from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

class UserSignupViewTestCase(APITestCase):
    def setUp(self):
        # Initializing the API client and defining the URL for user signup
        self.client = APIClient()
        self.signup_url = reverse("user-signup")

        # Defining valid and invalid payload data for testing
        self.valid_payload = {
            "username": "testuser",
            "password": "testpassword",
            "user_role": "OP",
        }
        self.empty_user_role_payload = {
            "username": "testuser",
            "password": "testpassword",
            "user_role": "",
        }

    # Testing user signup with valid data returns a successful response
    def test_valid_data_user_signup(self):
        response = self.client.post(self.signup_url, self.valid_payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # Testing user signup with an empty user role results in a bad request
    def test_user_signup_with_empty_role_results_in_bad_request(self):
        response = self.client.post(
            self.signup_url, self.empty_user_role_payload, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


