from django.db import models

class Activite(models.Model):
    intitule=models.CharField(max_length=200)
    date=models.DateField()

    def __str__(self):
        return "%s" %self.intitule