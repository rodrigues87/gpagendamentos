from django.contrib import admin
from residencia.models import *


class BlocoAdmin(admin.ModelAdmin):
    list_display = ['identificacao']
    filter_horizontal = ('residencias',)


class ResidenciaAdmin(admin.ModelAdmin):
    list_display = ['numero', 'bloco']
    filter_horizontal = ('morador',)


admin.site.register(Bloco, BlocoAdmin)
admin.site.register(Residencia, ResidenciaAdmin)
