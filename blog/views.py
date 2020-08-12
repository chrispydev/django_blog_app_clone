from blog.models import Post
from django.shortcuts import render
from django.views.generic import ListView, DetailView


class PostListView(ListView):
    model = Post
    context_object_name = 'posts'


class PostDetailView(DetailView):
    model = Post
    context_object_name = 'posts'
