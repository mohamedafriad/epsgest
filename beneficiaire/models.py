from django.db import models

class Beneficiaire(models.Model):
	nom=models.CharField(max_length=20, blank=True)
	prenom=models.CharField(max_length=20, blank=True)
	
	def __str__(self):
		return "%s %s" %(self.nom, self.prenom)
