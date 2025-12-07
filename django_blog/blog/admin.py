# blog/admin.py
from django.contrib import admin
from .models import Post, Profile
from .models import Comment
admin.site.register(Post)
admin.site.register(Profile)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'created_at')
    search_fields = ('author__username', 'content')
