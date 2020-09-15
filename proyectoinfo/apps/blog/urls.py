from django.urls import path
from . import views
from .views import DetalleNoticia, Listar, CrearNoticia

urlpatterns= [
	path('lista/', Listar.as_view(), name='lista'),
	path('', views.home, name='home'),
	path('<slug:pk>/detalle', DetalleNoticia.as_view(), name='detalle'),
	path('crear/', CrearNoticia.as_view(), name='crear')
]