from django.db import models
from user_mgn.models import User
from customer_mgn.models import Client, Maison

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
    TYPE_SPECIALITES_CHOICES = [
        ('menagere', 'Ménagère'),
        ('nounou', 'nounou'),
        ('assistant', 'assistant'),
        ('cuisinier', 'cuisinier')
    ]
    type_contrat = models.CharField(max_length=20, choices=TYPE_CONTRAT_CHOICES)
    specialite = models.CharField(max_length=25, choices=TYPE_SPECIALITES_CHOICES)
    taux_horaire = models.DecimalField(max_digits=6, decimal_places=2)
    clients = models.ManyToManyField(Client, through='Affectation', related_name='personnels')
    créé_par = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='personnels_crees')

    def __str__(self):
        return self.nom
    
class Position(models.Model):
    nom = models.CharField(max_length=255)
    maison = models.ForeignKey(Maison, on_delete=models.CASCADE)

class Affectation(models.Model):
    personnel = models.ForeignKey(Personnel, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    date_debut = models.DateField()
    date_fin = models.DateField()

    def __str__(self):
        return f'Affectation de {self.personnel} chez {self.client} à la position {self.position}'
    

