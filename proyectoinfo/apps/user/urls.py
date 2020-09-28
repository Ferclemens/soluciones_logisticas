from django.urls import path
from django.contrib.auth import views as auth_views
from .views import Registro 

urlpatterns=[
			path('registro/', Registro.as_view(), name='registro'),
			path('login/', auth_views.LoginView.as_view(), {'template_name':"login.html"}, name='login'),
			path('logout/', auth_views.logout_then_login,  name='logout'),
			]