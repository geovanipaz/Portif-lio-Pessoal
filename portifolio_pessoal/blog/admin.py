from django.contrib import admin
from .models import Categoria, Post, Comentario
# Register your models here.

admin.site.register(Categoria)
admin.site.register(Post)
admin.site.register(Comentario)
