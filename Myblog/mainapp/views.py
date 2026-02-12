from django.views.generic import ListView, DetailView
from .models import Post


class PostListView(ListView):
    model = Post
    template_name = 'mainapp/post_list.html'
    context_object_name = 'posts'
    ordering = ['-created_at']

    def get_queryset(self):
        return super().get_queryset().filter(status='published')


class PostDetailView(DetailView):
    model = Post
    template_name = 'mainapp/post_detail.html'
    context_object_name = 'post'
    slug_url_kwarg = 'slug'

    def get_queryset(self):
        return super().get_queryset().filter(status='published')
