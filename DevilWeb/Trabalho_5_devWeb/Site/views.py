from django.shortcuts import render, redirect, get_object_or_404
# Create your views here.
from .models import Images


def home(request):
    caminhos = {}
    for item in Images.objects.filter(nome__contains='Home'):
        caminhos[item.nome] = "images/" + item.caminho
    for item in Images.objects.filter(nome__contains='base'):
        caminhos[item.nome] = "images/" + item.caminho
    return render(request, 'Home/index.html', caminhos)


def noticia(request):
    caminhos = {}
    for item in Images.objects.filter(nome__contains='Home_Bar'):
        caminhos[item.nome] = "images/" + item.caminho
    for item in Images.objects.filter(nome__contains='noticia'):
        caminhos[item.nome] = "images/" + item.caminho
    for item in Images.objects.filter(nome__contains='base'):
        caminhos[item.nome] = "images/" + item.caminho
    return render(request, 'Noticia/noticia.html', caminhos)

def cadastro(request):
    caminhos = {}
    for item in Images.objects.filter(nome__contains='base'):
        caminhos[item.nome] = "images/" + item.caminho
    return render(request, 'Cadastro/cadastro.html', caminhos)
