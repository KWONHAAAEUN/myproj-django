import json
from django.http import HttpResponse
from rest_framework import viewsets
from lol.models import Post
from lol.serializers import PostSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset=Post.objects.all()
    serializer_class = PostSerializer

    def get_queryset(self):
        qs= super().get_queryset()

        query=self.request.query_params.get("query","")
        if query:
            qs=qs.filter(champion__icontains=query)

        return qs