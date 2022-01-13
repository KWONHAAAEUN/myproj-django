from django.db import models

class Post(models.Model):
    champion=models.CharField(max_length=30,db_index=True)
    role=models.CharField(max_length=20)
    photo=models.ImageField(blank=True)
    story=models.TextField()

    def __str__(self)->str:
        return self.champion
