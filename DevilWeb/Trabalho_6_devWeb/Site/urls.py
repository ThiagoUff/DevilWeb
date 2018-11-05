from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'Site'


urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('noticia/', views.noticia, name='noticia'),
    path('login/', views.login, name='login'),
    path('cadastrar/', views.cadastra_User, name='cadastra_User'),
    path('exibirUser/<int:id>/', views.exibe_user, name='exibe_user'),
    path('editar/<int:id>/', views.edita_user, name='edita_user'),
    path('remover/', views.remove_user, name='remove_user'),

]
