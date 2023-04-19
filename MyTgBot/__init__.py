
import logging

# enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('logs.txt'),
              logging.StreamHandler()],
    level=logging.INFO)


import os

api_id = os.getenv("API_ID")
api_hash = os.getenv("API_HASH")
bot_token = os.getenv("TOKEN")
group_id = os.getenv("GROUP_ID")


from pyrogram import Client

bot = Client("MyTgBot", 
       api_id=API_ID, 
       api_hash=API_HASH,
       bot_token=TOKEN,
       plugins=dict(root="MyTgBot"), )
