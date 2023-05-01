import requests

from MyTgBot import bot
from pyrogram import filters

BOT_ID = (6005606875)

@bot.on_message(filters.command("chatbot"))
async def chatbot(_, message):
         if message.reply_to_message:
             await message.reply("Successfully ChatBot Active!")
         return
             await message.reply("This Chat Already Enabled ChatBot!")
        
@bot.on_message(filters.text, group=200)
async def addchat(_, message):
          if not message.reply_to_message:
                return
          elif not message.reply_to_message.from_user.id == BOT_ID:
                return
          elif message.reply_to_message.from_user.id == BOT_ID:
               Message = message.text
               API = requests.get("https://kora-api.vercel.app/chatbot/2d94e37d-937f-4d28-9196-bd5552cac68b/Serena/Anonymous/message="+Message).json()
               await message.reply(API["reply"])
