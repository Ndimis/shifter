from django.db import models
from user_mgn.models import User

class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nom = models.CharField(max_length=255)
    email = models.EmailField()
    téléphone = models.CharField(max_length=20)
    adresse = models.TextField()
    créé_par = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='clients_crees')

class Maison(models.Model):
    adresse = models.TextField()
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    créé_par = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='maisons_crees')

class Demande(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    details_demande = models.TextField()
    statut = models.CharField(max_length=20)
    créé_par = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='demandes_crees')

class Contrat(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    personnel = models.ForeignKey('personnel_management.Personnel', on_delete=models.CASCADE)
    date_debut = models.DateField()
    date_fin = models.DateField()
    statut = models.CharField(max_length=20)
    créé_par = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='contrats_crees')
