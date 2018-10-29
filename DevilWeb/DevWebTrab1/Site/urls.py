from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
   ## url(r'^(?P<Materia_ID>[0-9]+)/$', views.Imagem, name='noticia'),
]