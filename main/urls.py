from django.urls import path
from .views import PostViewSet

urlpaterns = [
    path('posts/', PostViewSet.as_view()),
]