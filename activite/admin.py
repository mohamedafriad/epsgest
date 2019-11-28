from django.contrib import admin
from .models import Activite

@admin.register(Activite)
class ActiviteAdmin(admin.ModelAdmin):
    list_display=('intitule', 'date')