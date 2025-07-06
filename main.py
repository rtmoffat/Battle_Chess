from dotenv import load_dotenv
import os
import json
import berserk
from time import sleep
from helpers.helpers import json_datetime_encoder

load_dotenv(override=True)

LICHESS_PAT=os.environ.get("LICHESS_PAT")
CACHE_DIR=os.environ.get("CACHE_DIR")

#Create a client
session = berserk.TokenSession(token=LICHESS_PAT)
client = berserk.Client(session=session)

#Get bot list
bots_file=os.path.join(CACHE_DIR,'bots.json')
if not os.path.exists(bots_file):
    print("updating bots file")
    bots=list(client.bots.get_online_bots(limit=5))
    with open(bots_file,'w') as fh:
        json.dump(bots,fh,cls=json_datetime_encoder,indent=2)

sleep(2)

#game=client.challenges.create_ai(
#    level=1
#)

sleep(1)
games = client.games.get_ongoing()
gameId=games[0]['gameId']
print(games)
print(gameId)
sleep(1)
myMove=input("Enter move:")
move=client.board.make_move(gameId,myMove)
sleep(1)
games=client.games.get_ongoing(count=1)
print(games)
client=None
session.close()
