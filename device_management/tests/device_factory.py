import factory
from factory.django import DjangoModelFactory

from accounts.tests.user_factory import UserFactory
from device_management.models import Device, DeviceData

# Factory class for generating Device instances
class DeviceFactory(DjangoModelFactory):
    class Meta:
        model = Device

    # Using Faker to generate random values for fields
    name = factory.Faker("word")
    owner = factory.SubFactory(UserFactory)
    manufacturer = factory.Faker("company")
    serial_number = factory.Faker("random_number", digits=9)
    description = factory.Faker("paragraph")


# Factory class for generating DeviceData instances
class DeviceDataFactory(DjangoModelFactory):
    class Meta:
        model = DeviceData

    # Using SubFactory to create related Device instances and Faker for generating values
    device = factory.SubFactory(DeviceFactory)
    value = factory.Faker("pystr")
