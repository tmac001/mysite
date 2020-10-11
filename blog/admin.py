from django.contrib import admin
from .models import BlogType, Blog


@admin.register(BlogType)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'type_name')


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'author', 'blog_type',
                    'create_time', 'update_time')
