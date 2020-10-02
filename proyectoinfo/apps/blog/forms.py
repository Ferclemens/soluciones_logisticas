from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import *

class NoticiaForm(forms.ModelForm):
	class Meta:
		model= Noticia
		fields = ('autor', 'titulo', 'contenido')

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()


class ComentarioForm(forms.ModelForm):
	class Meta:
		model= Comentario
		fields = ('noticia','autor', 'fecha_hora', 'contenido')

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
