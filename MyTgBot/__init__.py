import os

api_id = os.getenv("API_ID")
api_hash = os.getenv("API_HASH")
bot_token = os.getenv("TOKEN")


from pyrogram import Client

bot = Client("MyTgBot", 
       api_id=api_id, 
       api_hash=api_hash,
       bot_token=bot_token,
       plugins=dict(root="MyTgBot"), )
