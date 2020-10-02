from django.contrib import admin
from .models import Noticia, Comentario


class NoticiaAdmin(admin.ModelAdmin):
	list_display = ('titulo', 'autor', 'fecha_creacion')
	list_filter = ('autor',)
# Register your models here.
admin.site.register(Noticia, NoticiaAdmin)

class ComentarioAdmin(admin.ModelAdmin):
	list_display = ('autor', 'contenido', 'fecha_hora')
	list_filter = ('autor',)

admin.site.register(Comentario, ComentarioAdmin)