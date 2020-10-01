from django.shortcuts import render, redirect
from .models import Usuario
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.views import generic
# Create your views here.

class Registro_form(UserCreationForm):
	class Meta(UserCreationForm.Meta):
		model = Usuario
		fields = ('username', 'email', 'password1', 'password2', "nombre","apellido","dni","fecha_nacimiento","telefono")

class Registro(generic.CreateView):
	form_class = Registro_form
	success_url = "home"
	template_name = "Registro.html"
