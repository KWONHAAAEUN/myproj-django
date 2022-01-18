from rest_framework import serializers
from lol.models import Post
from django.contrib.auth import get_user_model

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["username", "first_name", "last_name"]

class PostSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    class Meta:
        model=Post
        fields="__all__"

