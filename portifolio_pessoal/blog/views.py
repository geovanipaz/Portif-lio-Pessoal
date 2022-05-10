from django.shortcuts import render
from .models import Comentario, Post
# Create your views here.

def blog_index(request):
    posts = Post.objects.all()
    context = {
        'posts':posts
    }
    return render(request, 'blog/blog_index.html', context)

def blog_detalhe(request, pk):
    post = Post.objects.get(pk=pk)
    comentarios = Comentario.objects.filter(post=post)
    context = {
        'post':post,
        'comentatios': comentarios
    }
    return render(request, 'blog/blog_detalhe.html', context)