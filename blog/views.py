from django.views import generic
from django.contrib.auth.models import User
from .models import Blog, Author, Comment
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic.edit import CreateView


def index(request):
    users = User.objects.all().count()
    context = {
        'num_bloggers' : users
    }
    return render(request, 'index.html', context = context)

class BlogListView(generic.ListView):
    model = Blog
    paginate_by = 1

class BlogDetailView(generic.DetailView):
    model = Blog

class BloggerListView(generic.ListView):
    model = Author
    paginate_by = 2

class AuthorDetailView(generic.DetailView):
    model = Author

class AddComment(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ['comment_text', ]

    def get_context_data(self, **kwargs):
        """
        Add associated blog to form template so can display its title in HTML.
        """
        # Call the base implementation first to get a context
        context = super(AddComment, self).get_context_data(**kwargs)
        # Get the blog from id and add it to the context
        context['blog'] = get_object_or_404(Blog, pk=self.kwargs['pk'])
        return context

    def form_valid(self, form):
        """
        Add author and associated blog to form data before setting it as valid (so it is saved to model)
        """
        # Add logged-in user as author of comment
        form.instance.author = self.request.user
        # Associate comment with blog based on passed id
        form.instance.blog = get_object_or_404(Blog, pk=self.kwargs['pk'])
        # Call super-class form validation behaviour
        return super(AddComment, self).form_valid(form)

    def get_success_url(self):
        """
        After posting comment return to associated blog.
        """
        return reverse('blog-detail', kwargs={'pk': self.kwargs['pk'],})