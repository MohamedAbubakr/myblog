from django.views import generic
from django.contrib.auth.models import User
from .models import Blog, Author, Comment
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic.edit import CreateView
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm


def index(request):
    users = User.objects.all().count()
    context = {
        'num_bloggers': users
    }
    return render(request, 'index.html', context=context)


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


def draw(request):
    context = {
        'drawing': 'Draw here'
    }
    return render(request, 'blog/blog_draw.html', context=context)


class BlogListView(generic.ListView):
    model = Blog


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
        return reverse('blog-detail', kwargs={'pk': self.kwargs['pk'], })


class CreateAuthor(LoginRequiredMixin, CreateView):
    model = Author
    fields = ['name', 'bio', ]

    def form_valid(self, form):
        """
        Add author and associated blog to form data before setting it as valid (so it is saved to model)
        """
        # Add logged-in user as author of comment
        form.instance.author = self.request.user
        # Call super-class form validation behaviour
        return super(CreateAuthor, self).form_valid(form)

    def get_success_url(self):

        return reverse('bloggers')


class CreateBlog(LoginRequiredMixin, CreateView):
    model = Blog
    fields = ['post', 'description', 'author']

    def form_valid(self, form):
        # Call super-class form validation behaviour
        return super(CreateBlog, self).form_valid(form)

    def get_success_url(self):

        return reverse('blogs')
