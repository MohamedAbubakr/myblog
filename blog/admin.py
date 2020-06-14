from django.contrib import admin
from .models import Blog, Author, Comment

@admin.register(Blog)
class Blog(admin.ModelAdmin):
    list_display = ('post', 'author', 'date')
admin.site.register(Author)
@admin.register(Comment)
class Blog(admin.ModelAdmin):
    list_display = ('blog', 'comment_text', 'author', 'date')
