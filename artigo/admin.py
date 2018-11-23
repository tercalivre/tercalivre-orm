from django.contrib import admin
from .models import Artigo

class ArtigoAdmin(admin.ModelAdmin):
  prepopulated_fields = {'url': ('titulo', )}

admin.site.register(Artigo, ArtigoAdmin)