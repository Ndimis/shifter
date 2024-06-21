from django.db import models
from user_mgn.models import User

class Personnel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nom = models.CharField(max_length=255)
    email = models.EmailField()
    téléphone = models.CharField(max_length=20)
    adresse = models.TextField()
    TYPE_CONTRAT_CHOICES = [
        ('temps plein', 'Temps plein'),
        ('temps partiel', 'Temps partiel')
    ]
    type_contrat = models.CharField(max_length=20, choices=TYPE_CONTRAT_CHOICES)
    créé_par = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='personnels_crees')
