from django.contrib import admin
from .models import Blog, Author, Comment, Audio


@admin.register(Blog)
class Blog(admin.ModelAdmin):
    list_display = ('post', 'author', 'date')


admin.site.register(Author)
admin.site.register(Audio)


@admin.register(Comment)
class Blog(admin.ModelAdmin):
    list_display = ('blog', 'comment_text', 'author', 'date')
