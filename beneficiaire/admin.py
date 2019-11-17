from django.contrib import admin
from .models import *

@admin.register(Beneficiaire)
class BeneficiaireAdmin(admin.ModelAdmin):
	model=Beneficiaire
	list_display=('nom', 'prenom')
	search_fields=('nom', 'prenom')
