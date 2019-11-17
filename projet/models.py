from django.db import models

CHOIX_MILIEU=(
	('R', 'Rural'),
	('U', 'Urbain'),
)

class Projet(models.Model):
	nom=models.CharField(max_length=200)
	description=models.TextField(max_length=1000, blank=True, null=True)
	cout=models.DecimalField(null=True, blank=True, max_digits=10, decimal_places=2, verbose_name='Coût global')
	duree_exevution=models.CharField(max_length=20, verbose_name='Durée exécution en mois')
	lieu=models.CharField(max_length=200, verbose_name='Lieu implantation')
	milieu=models.CharField(max_length=100, choices=CHOIX_MILIEU)
