from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Author(models.Model):
    """Model representing an author."""
    name = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    bio = models.TextField()

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name.username

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('author-detail', args=[str(self.id)])


class Blog(models.Model):
    post = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField()
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        """String for representing the Model object."""
        return self.post

    def get_absolute_url(self):
        """Returns the url to access a detail record for this blog."""
        return reverse('blog-detail', args=[str(self.id)])


class Comment(models.Model):
    comment_text = models.TextField(null=False)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment_text

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('blogs')
