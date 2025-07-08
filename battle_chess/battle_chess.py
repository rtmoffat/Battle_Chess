from dotenv import load_dotenv
import os
import json
import berserk
from time import sleep
from helpers.helpers import json_datetime_encoder

load_dotenv(override=True)

LICHESS_PAT=os.environ.get("LICHESS_PAT")
CACHE_DIR=os.environ.get("CACHE_DIR")

class battle_chess_controller:
    def __init__(self):
        self.session=None
        self.client=None
    def connect(self,token:str):
        try:
            self.session = berserk.TokenSession(token=token)
            self.client = berserk.Client(session=self.session)
        except Exception as e:
            return {"Result":e}
        return {"Result":"Connected"}
    def listGames(self):
        try:
            games = self.client.games.get_ongoing()
        except Exception as e:
            return {"Exception":e}
        return games
if __name__ == "__main__":
    print("Import as module")
