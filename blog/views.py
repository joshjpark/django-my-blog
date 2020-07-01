from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

def home(request):
    context = {
        'posts' : Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

# list of posts view
class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

# individual post view
class PostDetailView(DetailView):
    model = Post

# individual post create view
class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content']

#  


def about(request):
    return render(request, 'blog/about.html', {'title' : 'About'})

