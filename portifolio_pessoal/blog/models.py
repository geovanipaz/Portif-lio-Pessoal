
from django.db import models

# Create your models here.

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.nome
    
class Post(models.Model):
    titulo = models.CharField(max_length=255)
    corpo = models.TextField()
    criado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)
    imagem = models.ImageField(upload_to='blog_imagens', null=True)
    categoria = models.ManyToManyField(Categoria, related_name='posts')
    
    def __str__(self) -> str:
        return self.titulo

class Comentario(models.Model):
    autor = models.CharField(max_length=60)
    corpo = models.TextField()
    criado = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, 
                             related_name='posts')
    
    def __str__(self) -> str:
        return self.autor