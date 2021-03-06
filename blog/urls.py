from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('all', views.BlogListView.as_view(), name='blogs'),
    path('<int:pk>', views.BlogDetailView.as_view(), name='blog-detail'),
    # path('<int:blog_id>/', views.blog_detail_view, name='blog-detail'),
    path('bloggers', views.BloggerListView.as_view(), name='bloggers'),
    path('blogger/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),
    # path('<int:pk>/comment', views.AddComment.as_view(), name='comment-form'),
    path('draw', views.draw, name='draw'),
    path('create_author', views.CreateAuthor.as_view(), name='author-create'),
    path('create_blog', views.CreateBlog.as_view(), name='blog-create'),
    path(r'^signup/$', views.signup, name='signup'),
    path('delete_comment/<int:comment_id>', views.delete_comment, name='comment-delete'),
    path('update_comment/<int:comment_id>', views.update_comment, name='comment-update'),
    path('audio/', views.AudioListView.as_view(), name='audio-list'),
    path('audio/add_audio', views.add_audio, name='add-audio'),
]
