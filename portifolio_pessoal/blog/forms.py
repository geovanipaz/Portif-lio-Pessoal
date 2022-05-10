from django import forms
from .models import Post, Comentario


class FormPost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo','corpo', 'imagem', 'categoria']