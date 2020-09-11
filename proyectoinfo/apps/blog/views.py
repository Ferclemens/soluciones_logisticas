from django.shortcuts import render
from .models import Noticia
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

# Create your views here.

class Listar(ListView):
	model=Noticia
	template_name = "listar_noticias.html"
	context_object_name = "noticias"

def home(request):
	return render(request, 'home.html', {})


class DetalleNoticia(DetailView):
	model=Noticia
	template_name="detalle_noticia.html"





