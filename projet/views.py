from django.shortcuts import render
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Projet

class CreerProjet(CreateView):
	model=Projet
	template_name="nouveau_projet.html"
	fields=('nom', 'description', 'cout', 'milieu', 'duree_execution')
	success_url="/projet/"


class ListProjet(ListView):
	model=Projet
	context_object_name="projets"
	template_name="list_projet.html"


class DetailProjet(DetailView):
	model=Projet
	context_object_name="projet"
	template_name="detail_projet.html"


class EditerProjet(UpdateView):
	model=Projet
	context_object_name="projet"
	template_name="editer_projet.html"
	fields=('nom', 'description', 'cout', 'milieu', 'duree_execution')



class DeleteProjet(DeleteView):
	model=Projet
	template_name="supprimer_projet.html"
	success_url="/projet/"
