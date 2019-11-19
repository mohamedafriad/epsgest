from django.contrib import admin
from .models import Projet

@admin.register(Projet)
class ProjetAdmin(admin.ModelAdmin):
	model=Projet
	list_display=('nom', 'cout', 'milieu')
	list_filter=('milieu',)

