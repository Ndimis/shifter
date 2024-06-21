from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    créé_par = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='utilisateurs_crees')

