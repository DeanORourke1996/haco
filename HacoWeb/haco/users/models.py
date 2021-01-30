from django.db import models
from django.contrib.auth.models import User as Usr


# Create your models here.
class User(models.Model):
    username = models.OneToOneField(Usr, on_delete=models.CASCADE, primary_key=True, max_length=50)
    email = models.EmailField(max_length=150)
    password = models.CharField(max_length=150)

    def __str__(self):
        return f"{self.user}"
