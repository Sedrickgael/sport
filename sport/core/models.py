from django.db import models
from django.conf import global_settings
from django.utils import timezone

# Create your models here.

class Equipe(models.Model):
	nom = models.CharField(max_length=200)
	point = models.FloatField()
	championat=models.CharField(max_length=200)



class Compte(models.Model):
	solde = models.FloatField()



class Match(models.Model):
	domicile = models.CharField(max_length=200)
	exterieur = models.CharField(max_length=200)
	domicile_cote = models.FloatField()
	exterieur = models.FloatField()
	nul_cote = models.FloatField()
	championat=models.CharField(max_length=200)

	