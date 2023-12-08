from django.contrib import admin
from django.urls import include, path
# from drf_yasg import openapi
# from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

# schema_view = get_schema_view(
#     openapi.Info(
#         title="IOT Device Management Backend API Documentation",
#         default_version="v1",
#         description="API for the iot device management",
#         terms_of_service="https://www.yourapp.com/terms/",
#         contact=openapi.Contact(email="contact@gmail.com"),
#     ),
#     public=True,
#     permission_classes=[permissions.AllowAny],
# )


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    # path(
    #     "swagger<str:format>",
    #     schema_view.without_ui(cache_timeout=0),
    #     name="schema-json",
    # ),
    # path(
    #     "api/swagger/",
    #     schema_view.with_ui("swagger", cache_timeout=0),
    #     name="schema-swagger-ui",
    # ),
    # path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    # Optional UI:
    path(
        "api/schema/swagger-ui/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/schema/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
    path('', include('device_management.urls')),
    path('', include('accounts.urls')),
]
