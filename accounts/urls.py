from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, LoginView, SignupView

router = DefaultRouter()
router.register(r"users", UserViewSet, basename="user")

urlpatterns = [
    path("api/", include(router.urls)),
    path("api/users/login/", LoginView.as_view(), name="user-login"),
    path("api/users/signup/", SignupView.as_view(), name="user-signup"),
]
