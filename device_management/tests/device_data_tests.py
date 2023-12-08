from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from accounts.tests.user_factory import UserFactory
from .device_factory import DeviceFactory, DeviceDataFactory
from accounts.tests.user_login_tests import UserLoginViewTestCase
from device_management.serializer import DeviceDataSerializer

class DeviceDataTestCase(UserLoginViewTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.client = APIClient()

    def setUp(self):
        super().setUp()
        self.user = UserFactory()
        self.device = DeviceFactory.create(owner=self.user)
        self.device_data = DeviceDataFactory.create(device=self.device)
        self.test_successful_login_returns_access_token()
        self.access_token = self.access_token
        self.header = {"Authorization": f"Bearer {self.access_token}"}

    def make_api_request(self, method, url, data=None):
        if method == "post":
            return self.client.post(url, data, format="json", headers=self.header)
        elif method == "get":
            return self.client.get(url, format="json", headers=self.header)
        elif method == "patch":
            return self.client.patch(url, data, format="json", headers=self.header)
        elif method == "delete":
            return self.client.delete(url, headers=self.header)

    def test_create_device_data(self):
        data = DeviceDataFactory.build(device=self.device)
        serializer = DeviceDataSerializer(data)
        response = self.make_api_request("post", reverse("device-data-list"), serializer.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_device_data(self):
        url = reverse("device-data-detail", kwargs={"pk": self.device_data.id})
        response = self.make_api_request("get", url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["value"], self.device_data.value)

    def test_update_device_data(self):
        url = reverse("device-data-detail", kwargs={"pk": self.device_data.id})
        updated_data = DeviceDataFactory.build(device=self.device, value="Updated Value")
        serializer = DeviceDataSerializer(updated_data)
        response = self.make_api_request("patch", url, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["value"], "Updated Value")

    def test_delete_device_data(self):
        url = reverse("device-data-detail", kwargs={"pk": self.device_data.id})
        response = self.make_api_request("delete", url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
