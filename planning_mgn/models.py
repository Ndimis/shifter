from django.db import models

from user_mgn.models import User
from customer_mgn.models import Client, Maison
from personnel_mgn.models import Personnel

class Planning(models.Model):
    personnel = models.ForeignKey(Personnel, on_delete=models.CASCADE, related_name='plannings')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='plannings')
    titre = models.CharField(max_length=255)
    date_debut = models.DateField()
    date_fin = models.DateField()

    def __str__(self):
        return f'{self.titre} pour {self.personnel} chez {self.client}'

class JourneeDeTravail(models.Model):
    planning = models.ForeignKey(Planning, on_delete=models.CASCADE, related_name='journees')
    date = models.DateField()
    heure_debut = models.TimeField()
    heure_fin = models.TimeField()

    def heures_effectives(self):
        return (self.heure_fin - self.heure_debut).seconds / 3600

    def __str__(self):
        return f'Journee de travail le {self.date} pour {self.planning}'

class Presence(models.Model):
    journee = models.ForeignKey(JourneeDeTravail, on_delete=models.CASCADE, related_name='presences')
    est_present = models.BooleanField(default=True)
    heure_arrivee = models.TimeField(null=True, blank=True)
    heure_depart = models.TimeField(null=True, blank=True)
    remarques = models.TextField(blank=True, null=True)

    def heures_travail(self):
        if self.heure_arrivee and self.heure_depart:
            return (self.heure_depart - self.heure_arrivee).seconds / 3600
        return 0

    def __str__(self):
        return f'{self.journee.planning.personnel} - {self.journee.date} - {"Présent" if self.est_present else "Absent"}'

class Tache(models.Model):
    planning = models.ForeignKey(Planning, on_delete=models.CASCADE)
    description = models.TextField()
    statut = models.CharField(max_length=20)
    créé_par = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='taches_crees')
