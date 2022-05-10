from django.urls import path
from . import views


app_name = 'projetos'

urlpatterns = [
    path('', views.projetos_index, name='index'),
    path('<pk>/', views.projeto_detalhe, name='detalhe'),
]
