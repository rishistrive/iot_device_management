from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from accounts.tests.user_login_tests import UserLoginViewTestCase
from accounts.tests.user_factory import UserFactory
from .device_factory import DeviceFactory


class DeviceViewSetTestCase(APITestCase, UserLoginViewTestCase):
    device_data = {
        "name": "Test Device",
        "owner": UserFactory().id,
        "manufacturer": "Test Manufacturer",
        "serial_number": "SN123",
        "description": "Test Description",
    }

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.device = DeviceFactory()
        cls.device_url = reverse("device-list")

    def setUp(self):
        super().setUp()
        self.headers = {"Authorization": f"Bearer {self.access_token}"}

    def make_api_request(self, method, url, data=None):
        if method == "post":
            return self.client.post(url, data, format="json", headers=self.headers)
        elif method == "get":
            return self.client.get(url, format="json", headers=self.headers)
        elif method == "patch":
            return self.client.patch(url, data, format="json", headers=self.headers)
        elif method == "delete":
            return self.client.delete(url, headers=self.headers)

    def test_create_device_authenticated_user(self):
        response = self.make_api_request("post", self.device_url, self.device_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_device(self):
        url = reverse("device-detail", kwargs={"pk": self.device.id})
        response = self.make_api_request("get", url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_device(self):
        url = reverse("device-detail", kwargs={"pk": self.device.id})
        updated_data = {
            "name": "Updated Device Name",
            "description": "Updated Device Description",
        }
        response = self.make_api_request("patch", url, updated_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], updated_data["name"])

    def test_delete_device(self):
        url = reverse("device-detail", kwargs={"pk": self.device.id})
        response = self.make_api_request("delete", url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
