from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('noticia', views.noticia, name='noticia'),
    path('cadastro',views.cadastro, name = 'cadastro')
]
