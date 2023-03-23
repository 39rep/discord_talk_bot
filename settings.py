from dotenv import load_dotenv
import os
from os.path import join, dirname

def base():
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)

def getToken():
    base()
    DIS_TOKEN = os.environ.get("DISCORD_BOT_TOKEN")
    return DIS_TOKEN

def getId():
    base()
    SERVER_ID = os.environ.get("SERVER_ID")
    return SERVER_ID

def getKey():
    base()
    API_KEY = os.environ.get("OPENAI_API_KEY")
    return API_KEY
