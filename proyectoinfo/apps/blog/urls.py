from django.urls import path
from . import views

urlpatterns= [
	path('lista/', views.listar_noticias, name='lista'),
	path('', views.home, name='home'),
]