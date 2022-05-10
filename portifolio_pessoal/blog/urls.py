from django.urls import path
from . import views


app_name = 'blog'

urlpatterns = [
    path('', views.blog_index, name='index'),
    path('<pk>/',views.blog_detalhe, name='detalhe'),
]