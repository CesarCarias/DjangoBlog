from django.shortcuts import render
from django.views.generic import ListView
from blogs.models import Post

# Create your views here.
class BlogListView(ListView):
    model = Post
    template_name = "home.html"
    