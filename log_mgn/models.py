from django.db import models

from user_mgn.models import User

class Log(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    action = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    details = models.TextField(null=True, blank=True)

