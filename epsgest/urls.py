"""epsgest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic.edit import DeleteView
from django.views.generic.base import TemplateView
from beneficiaire.models import Beneficiaire
from beneficiaire.views import ListBeneficiaire, DetailBeneficiaire, CreerBeneficiaire, UpdateBeneficiaire
from projet.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name="accueil.html"), name="accueil"),
    path('beneficiaire/', ListBeneficiaire.as_view(template_name="list_benef_grid.html"), name="list_beneficiaire"),
    path('beneficiaire/table/', ListBeneficiaire.as_view(template_name="list_benef_table.html"), name="list_beneficiaire"),
    path('beneficiaire/<int:pk>/', DetailBeneficiaire.as_view(), name="detail_beneficiaire"),
    path('beneficiaire/ajout/', CreerBeneficiaire.as_view(), name="creer_beneficiaire"),
    path('beneficiaire/<int:pk>/editer/', UpdateBeneficiaire.as_view(), name="update_beneficiaire"),
    path('beneficiaire/<int:pk>/supprimer/', DeleteView.as_view(model=Beneficiaire, success_url="/beneficiaire/"), name="supprimer_beneficiaire"),
    path('projet/', ListProjet.as_view(), name="list_projet"),
    path('projet/<int:pk>/', DetailProjet.as_view(), name="detail_projet"),
    path('projet/ajout/', CreerProjet.as_view(), name="ajout_projet"),
    path('projet/<int:pk>/editer/', EditerProjet.as_view(), name="editer_projet"),
    path('projet/<int:pk>/supprimer/', DeleteProjet.as_view(), name="supprimer_projet"),
]
