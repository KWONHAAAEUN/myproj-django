from django.contrib import admin

from lol.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass