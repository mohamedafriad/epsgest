from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse
from .models import Beneficiaire

class ListBeneficiaire(ListView):
	queryset=Beneficiaire.objects.all()
	context_object_name="beneficiaires"
	paginate_by=20
	template_name="list_benef.html"

class DetailBeneficiaire(DetailView):
	queryset=Beneficiaire.objects.all()
	context_object_name="beneficiaire"
	template_name="detail_benef.html"
	
	def get_object(self):
	    obj=super().get_object()
	    return obj

class CreerBeneficiaire(CreateView):
	model=Beneficiaire
	fields=['nom', 'prenom', 'sexe']
	success_url="/beneficiaire/"

class UpdateBeneficiaire(UpdateView):
	model=Beneficiaire
	fields=['nom', 'prenom', 'sexe']
	success_url="/beneficiaire/"