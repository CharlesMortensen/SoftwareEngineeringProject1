from django.db import models
from enum import Enum

# Create your models here.

class Player(models.Model):
    id = models.IntegerField(primary_key=True, blank=False, null=False)
    first_name = models.CharField(max_length=30, blank=False, null=False)
    last_name = models.CharField(max_length=30, blank=False, null= False)
    codename = models.CharField(max_length=30, blank=False, null=False, unique=True)

    def __str__(self):
        return str(self.id)
    
class ActivePlayer(models.Model):
    # Team colors
    RED = "RED"
    BLUE = "BLUE"
    TEAM_CHOICES = [
        (RED, "Red"),
        (BLUE, "Blue"),
    ]

    player_info = models.ForeignKey("Player", on_delete=models.CASCADE)
    team = models.CharField(max_length=4, choices=TEAM_CHOICES)

    def __str__(self):
        return f"{self.player_info.id}, {self.team}"