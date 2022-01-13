from django.urls import path,include
from rest_framework.routers import DefaultRouter

from lol import views
from lol.views import PostViewSet

app_name = 'lol'

router=DefaultRouter()
router.register("posts",PostViewSet)

urlpatterns = [
    # path("posts.json", views.post_list),
    path("api/", include(router.urls)),
]