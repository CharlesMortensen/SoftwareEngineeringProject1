import websocket
import random
import time
from argparse import ArgumentParser

# Get positive integer input
def get_int(message: str) -> int:
    while True:
        try:
            val = int(input(message))
            if val < 0:
                raise ValueError
            return val
        except ValueError:
            print("Input must be a positive integer")

parser = ArgumentParser(description="Sends player action data over websocket")
parser.add_argument("-d", "--domain", dest="domain", default="team2-lasertag.herokuapp.com", help="Set a different domain to send traffic to. Be sure to specify port number if running locally, e.g. 'localhost:8000'")
args = parser.parse_args()

print('this program will generate some test traffic for 2 players on the red ')
print('team as well as 2 players on the green team')
print('')

red1 = get_int('Enter id of red player 1 ==> ')
red2 = get_int('Enter id of red player 2 ==> ')
green1 = get_int('Enter id of green player 1 ==> ')
green2 = get_int('Enter id of green player 2 ==> ')

print('')
counter = get_int('How many events do you want ==> ')

# Create socket
socket = websocket.WebSocket()
socket.connect(f"ws://{args.domain}/ws/guns/")

# Counter for number of events, with random player and order
for _ in range(counter):
    redplayer = red1 if random.choice([True, False]) else red2
    greenplayer = green1 if random.choice([True, False]) else green2
    message = f"{redplayer}:{greenplayer}" if random.choice([True, False]) else f"{greenplayer}:{redplayer}"

    print(message)
    socket.send(message)
    time.sleep(random.randint(1, 3))

socket.close()
print("program complete")
