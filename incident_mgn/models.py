from django.db import models

# Create your models here.
from user_mgn.models import User
from personnel_mgn.models import Personnel
from customer_mgn.models import Client, Maison

class Incident(models.Model):
    personnel = models.ForeignKey(Personnel, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    lieu = models.ForeignKey(Maison, on_delete=models.CASCADE)
    description = models.TextField()
    date = models.DateField()
    créé_par = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='incidents_crees')