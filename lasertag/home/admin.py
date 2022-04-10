from django.contrib import admin
from .models import LaserTagMessage, Player, ActivePlayer
# Register your models here.

admin.site.register(Player)
admin.site.register(ActivePlayer)
admin.site.register(LaserTagMessage)