import json
from django.http import HttpResponse
from rest_framework import viewsets
from lol.models import Post
from lol.serializers import PostSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset=Post.objects.all()
    serializer_class = PostSerializer
