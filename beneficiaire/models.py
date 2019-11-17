from django.db import models

CHOIX_SEXE=(
	('M', 'Masuclin'),
	('F', 'Féminin'),
)

class Beneficiaire(models.Model):
	nom=models.CharField(max_length=20, blank=True)
	prenom=models.CharField(max_length=20, blank=True)
	sexe=models.CharField(max_length=20, blank=True, choices=CHOIX_SEXE)

	def nom_prenom(self):
		return self.__str__()
	
	def __str__(self):
		return "%s %s" %(self.nom, self.prenom)
