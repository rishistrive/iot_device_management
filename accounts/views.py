from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import User
from .serializer import TokenSerializer, UserSerializer


class SignupView(CreateAPIView):
    """
    View for user registration, allowing any user to sign up.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class UserViewSet(ModelViewSet):
    """
    Viewset for managing user-related operations with authentication required.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class LoginView(TokenObtainPairView):
    """
    View for handling user authentication and token generation.
    """

    serializer_class = TokenSerializer
    permission_classes = [AllowAny]
