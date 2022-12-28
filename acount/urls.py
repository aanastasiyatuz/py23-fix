from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import RegisterUserView


urlpatterns = [
    path('register/', RegisterUserView),
    path('login/', TokenObtainPairView),
    path('refresh/', TokenRefreshView),
]