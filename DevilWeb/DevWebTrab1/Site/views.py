from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Imagem


def index(request):
    noticias = Imagem(noticia=0)
    noticia = noticia()
    noticias = []
    return render(request, 'Site/index.html', {'noticias': noticias})


def noticias(request, Materia_ID):
    question = get_object_or_404(Imagem, noticia=Materia_ID)
    return render(request, 'Site/html/index.html', {'question': question})
