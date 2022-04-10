from channels.generic.websocket import WebsocketConsumer

class LasergunConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
    
    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        print("hello world")
        self.send(text_data="hello world")