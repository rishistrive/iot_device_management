from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import User


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the User model.
    """

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "password", "user_role"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        """
        Custom create method to create a user instance with the provided data.
        """
        return User.objects.create_user(**validated_data)


class TokenSerializer(TokenObtainPairSerializer):
    """
    Token serializer with additional field for user_role.
    """

    user_role = serializers.CharField(source="user.user_role", read_only=True)

    def validate(self, attrs):
        """
        Custom validate method to include user_role in the serialized output.
        """
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data["user_role"] = self.user.user_role
        data["refresh"], data["access"] = str(refresh), str(refresh.access_token)
        return data
