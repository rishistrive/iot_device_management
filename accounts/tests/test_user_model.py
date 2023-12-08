from django.contrib.auth.hashers import make_password
from django.test import TestCase

from .user_factory import UserFactory

class UserTestCase(TestCase):
    def test_user_password_hashing(self):
        # Creating a user instance using the UserFactory
        user = UserFactory()
        original_password = user.password

        # Updating the user password using make_password
        user.password = make_password(original_password)
        user.save()

        # Checking if the password is hashed correctly
        self.assertEqual(user.check_password(original_password), True)

    def test_user_roles(self):
        # Creating user instances with different roles using the UserFactory methods
        operator_user = UserFactory.operator()
        engineer_user = UserFactory.engineer()
        manager_user = UserFactory.manager()
        owner_user = UserFactory.owner()

        # Checking user roles for correctness
        self.assertEqual(operator_user.user_role, "OP")
        self.assertEqual(engineer_user.user_role, "ER")
        self.assertEqual(manager_user.user_role, "MR")
        self.assertEqual(owner_user.user_role, "OR")
