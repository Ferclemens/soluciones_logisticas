from django.urls import path
from . import views
from .views import DetalleNoticia, Listar, CrearNoticia, UpdateNoticia, DeleteNoticia, CrearOferta, ListarOfertas

urlpatterns= [
	path('lista/', Listar.as_view(), name='lista'),
	path('', views.home, name='home'),
	path('<slug:pk>/detalle', DetalleNoticia.as_view(), name='detalle'),
	path('<slug:pk>/update', UpdateNoticia.as_view(), name='update'),
	path('<slug:pk>/delete', DeleteNoticia.as_view(), name='delete'),
	path('crear/', CrearNoticia.as_view(), name='crear'),
	path('crear_oferta/', CrearOferta.as_view(), name='oferta'),
	path('listar_ofertas/', ListarOfertas.as_view(), name='lista_ofertas')
]