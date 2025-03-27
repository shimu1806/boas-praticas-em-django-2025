from django.contrib import admin
from .models import Local

@admin.register(Local)
class LocalAdmin(admin.ModelAdmin):
    list_display = ('nome', 'categoria', 'habilitado')
    list_filter = ('categoria', 'habilitado')
    search_fields = ('nome',)