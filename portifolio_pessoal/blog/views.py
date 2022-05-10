from multiprocessing import context
from django.shortcuts import redirect, render
from .models import Comentario, Post
from .forms import FormPost
from django.contrib import messages
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

def cria_post(request):
    form = FormPost()
    if request.method == 'POST':
        form = FormPost(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post criado com sucesso')
            return redirect('blog:index')
    context = {
        'form':form
    }
    return render(request, 'blog/cria_post.html', context)