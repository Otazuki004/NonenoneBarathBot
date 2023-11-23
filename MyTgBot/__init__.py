from pyrogram import Client
from pymongo import MongoClient
import os
import time

start = time.time()
version = "0.0.1"

api_id = os.getenv("API_ID")
api_hash = os.getenv("API_HASH")
bot_token = os.getenv("TOKEN")


bot = Client("MyTgBot", 
       api_id=api_id, 
       api_hash=api_hash,
       bot_token=bot_token,
       plugins=dict(root="MyTgBot"), )

MONGO = "mongodb+srv://pyrobot:Wpch7CTLJ2zd6tHo@cluster0.qlefbre.mongodb.net/?retryWrites=true&w=majority"
mongo = MongoClient(MONGO)
mongodb = mongo.BOT
