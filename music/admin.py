from django.contrib import admin
from .models import Artiste, Chanson

@admin.register(Artiste)
class ArtisteAdmin(admin.ModelAdmin):
    list_display = ('nom',)
    search_fields = ('nom',)

@admin.register(Chanson)
class ChansonAdmin(admin.ModelAdmin):
    list_display = ('titre', 'artiste')
    search_fields = ('titre', 'artiste__nom')
    list_filter = ('artiste',)