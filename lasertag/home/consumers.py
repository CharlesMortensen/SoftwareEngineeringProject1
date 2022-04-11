from channels.generic.websocket import WebsocketConsumer
from .models import LaserTagMessage, ActivePlayer, Player
import re
import json

class Game():
    redpoints = 0
    for x in ActivePlayer.objects.filter(team=ActivePlayer.RED):
        redpoints = redpoints + x.points 
    bluepoints = 0
    for x in ActivePlayer.objects.filter(team=ActivePlayer.BLUE):
        bluepoints = bluepoints + x.points 
    is_running = False

    def start():
        Game.is_running = True
        Game.redpoints = 0
        Game.bluepoints = 0
        ActivePlayer.objects.update(points=0)
        LaserTagMessage.objects.all().delete()
    
    def end():
        Game.is_running = False
        Game.redpoints = 0
        Game.bluepoints = 0
        ActivePlayer.objects.update(points=0)
        LaserTagMessage.objects.all().delete()

class LasergunConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
    
    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        print(text_data)
        if not Game.is_running:
            return
        players = re.findall(r'\d+', text_data)
        if len(players) != 2:
            return
        active1, active2 = int(players[0]), int(players[1])
        if not ActivePlayer.objects.filter(player_info=Player(pk=active1)).exists() or not ActivePlayer.objects.filter(player_info=Player(pk=active2)).exists():
            return
        active1 = ActivePlayer.objects.get(player_info=Player(pk=active1))
        active2 = ActivePlayer.objects.get(player_info=Player(pk=active2))
        active1.points += 1
        active1.save()
        if active1.team == ActivePlayer.RED:
            Game.redpoints += 1
        else:
            Game.bluepoints += 1
        message = LaserTagMessage(player1=active1, player2=active2)
        message.save()

class GameActionConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        # TODO: This will delete all messages when we disconnect
        #LaserTagMessage.objects.all().delete()
        pass
    
    def receive(self, text_data):
        messages = LaserTagMessage.objects.filter(message_isnew=True)
        combatlog = [f"{message.player1} hit {message.player2}!" for message in messages]
        ids = dict()
        for message in messages:
            ids[f"{message.player1.player_info.id}"] = message.player1.points
            ids[f"{message.player2.player_info.id}"] = message.player2.points
        data = json.dumps({'messages': combatlog, 'ids': ids, 'redpoints': Game.redpoints, 'bluepoints': Game.bluepoints})
        self.send(data)
        LaserTagMessage.objects.update(message_isnew=False)

class GameControlConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        if text_data == "start":
            Game.start()
        elif text_data == "end":
            Game.end()