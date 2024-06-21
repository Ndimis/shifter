from django.db import models

from user_mgn.models import User
from customer_mgn.models import Client
from personnel_mgn.models import Personnel

class Facture(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    mois = models.DateField()
    date_emission = models.DateField()
    date_paiement = models.DateField()
    statut = models.CharField(max_length=20)
    créé_par = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='factures_crees')

class BulletinDePaie(models.Model):
    personnel = models.ForeignKey(Personnel, on_delete=models.CASCADE)
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    date_emission = models.DateField()
    créé_par = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='bulletins_crees')
