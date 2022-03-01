from pyexpat import model
from django.db import models

# Create your models here.

class Player(models.Model):
    id = models.IntegerField(primary_key=True, blank=False, null=False)
    first_name = models.CharField(max_length=30, blank=False, null=False)
    last_name = models.CharField(max_length=30, blank=False, null= False)
    codename = models.CharField(max_length=30, blank=False, null=False, unique=True)


    def __str__(self):
        return str(self.id)