import factory

from accounts.models import User

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    # Using Faker to generate random username, first name, and last name
    username = factory.Faker("user_name")
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    password = factory.PostGenerationMethodCall("set_password", "testpassword")
    user_role = "OR"  # Default user role

    # Factory methods to create User instances with specific roles
    @classmethod
    def operator(cls):
        return cls(user_role="OP")

    @classmethod
    def engineer(cls):
        return cls(user_role="ER")

    @classmethod
    def manager(cls):
        return cls(user_role="MR")

    @classmethod
    def owner(cls):
        return cls(user_role="OR")
