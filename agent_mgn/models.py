from django.db import models
from user_mgn.models import User

class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nom = models.CharField(max_length=255)
    email = models.EmailField()
    téléphone = models.CharField(max_length=20)
    créé_par = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='agents_crees')
