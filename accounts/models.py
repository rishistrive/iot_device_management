from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    class Roles(models.TextChoices):
        OPERATOR = "OP", "Level Operator"
        ENGINEER = "EN", "Level Engineer"
        MANAGER = "MR", "Level Manager"
        OWNER = "OR", "Owner"

    user_role = models.CharField(max_length=2, choices=Roles.choices)

