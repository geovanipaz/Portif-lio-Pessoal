from django.db import models

# Create your models here.

class Projeto(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    tecnologia = models.CharField(max_length=30)
    imagem = models.ImageField(upload_to='projeto_imagens')
    
    def __str__(self) -> str:
        return self.titulo