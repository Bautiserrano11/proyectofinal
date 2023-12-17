# blogapp/views.py
from django.shortcuts import render, get_object_or_404
from .models import Post, Category

def all_posts(request):
    posts = Post.objects.all()
    return render(request, 'blogapp/all_posts.html', {'posts': posts})

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'blogapp/post_detail.html', {'post': post})
from django.shortcuts import render

def Homepage(request):
    posts = Post.objects.all()
    return render(request, 'blogapp/homepage.html', {'posts': posts})

