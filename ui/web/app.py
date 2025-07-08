import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.parent))
print(sys.path)

from battle_chess.battle_chess import battle_chess_controller

from flask import Flask
from flask_cors import CORS
import json
import os

from dotenv import load_dotenv

load_dotenv(dotenv_path='../.env', override=True)

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/connect")
def connect():
    token=os.environ.get('LICHESS_PAT')
    bc=battle_chess_controller()
    res=bc.connect(token=token)
    return json.dumps(res)

@app.route("/games")
def listGames():
    token=os.environ.get('LICHESS_PAT')
    bc=battle_chess_controller()
    bc.connect(token=token)
    res=bc.listGames()
    return json.dumps(res)