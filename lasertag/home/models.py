from django.db import models

# Create your models here.

class Player(models.Model):
    id = models.IntegerField(primary_key=True, blank=False, null=False)
    first_name = models.CharField(max_length=30, blank=False, null=False)
    last_name = models.CharField(max_length=30, blank=False, null= False)
    codename = models.CharField(max_length=30, blank=False, null=False)

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

    player_info = models.OneToOneField("Player", on_delete=models.CASCADE)
    team = models.CharField(max_length=4, choices=TEAM_CHOICES)
    points = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.player_info.id}, {self.team}"
    
class LaserTagMessage(models.Model):
    id = models.AutoField(primary_key=True)
    player1 = models.ForeignKey("ActivePlayer", related_name="player1_reference", on_delete=models.CASCADE)
    player2 = models.ForeignKey("ActivePlayer", related_name="player2_reference", on_delete=models.CASCADE)
    message_isnew = models.BooleanField(default=True)

