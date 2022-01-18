from django.conf import settings
from django.db import models

class Post(models.Model):
    champion=models.CharField(max_length=30,db_index=True)
    role=models.CharField(max_length=20)
    photo=models.ImageField(blank=True)
    story=models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)

    def __str__(self)->str:
        return self.champion
