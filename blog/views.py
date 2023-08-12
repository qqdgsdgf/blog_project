# blog/views.py
from django.views.generic import ListView, DetailView  # new
from django.views.generic.edit import CreateView, UpdateView, DeleteView  # new
from blog.models import PostDB
from django.urls import reverse_lazy


class BlogListView(ListView):
    model = PostDB
    template_name = 'home.html'

class BlogDetailView(DetailView):  # new
    model = PostDB
    template_name = 'post_detail.html'

class BlogCreateView(CreateView):  # new
    model = PostDB
    template_name = 'post_new.html'
    fields = ['title', 'author', 'body']

class BlogUpdateView(UpdateView):  # new
    model = PostDB
    template_name = 'post_edit.html'
    fields = ['title', 'body']

class BlogDeleteView(DeleteView):  # new
    model = PostDB
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')