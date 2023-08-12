# coding=utf-8
from django.urls import path
from blog.views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView

urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),  # new
    path('post/new/', BlogCreateView.as_view(), name='post_new'),  # new
    path('post/<int:pk>/edit/', BlogUpdateView.as_view(), name='post_edit'),  # new
]