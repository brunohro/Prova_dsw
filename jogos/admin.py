from django.contrib import admin
from .models import *

admin.site.register(Modalidade)
admin.site.register(Tecnico)

@admin.register(Atleta)
class AtletaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'matricula', 'equipe')
    list_filter = ('equipe',)
    search_fields = ('nome',)


@admin.register(Equipe)
class EquipeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'curso',)




