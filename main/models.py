from django.db import models
from acount.models import User

class Post(models.Manager):
    author = models.ForeignKey(User, related_name='posts')
    title = models.CharField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
