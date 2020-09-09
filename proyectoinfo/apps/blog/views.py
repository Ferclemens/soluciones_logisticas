from django.shortcuts import render
from .models import Noticia
# Create your views here.

def listar_noticias(request):
	noticias = Noticia.objects.all()
	context={}
	context['noticias']=noticias
	return render(request, 'listar_noticias.html', context)

def home(request):
	return render(request, 'home.html', {})