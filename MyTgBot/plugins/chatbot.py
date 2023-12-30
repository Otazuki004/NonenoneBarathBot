import requests
from pyrogram import filters
from pyrogram.types import *
from MyTgBot import bot
from pyrogram import enums

@bot.on_message(filters.reply, filters.private & filters.group)
async def chatbot(_, message):
    if message.chat.type == "private":
        if not message.reply_to_message:
            return
        if message.reply_to_message.from_user.id != (await bot.get_me()).id:
            return
    if message.text and message.text[0] in ["/", "!", "?", "."]:
        return
    await bot.send_chat_action(message.chat.id, enums.ChatAction.TYPING)
    
    response = requests.get(f"https://pervert-api.onrender.com/chatbot/{message.text}")
    if response.status_code == 200:
        try:
            results = response.json()
            await message.reply_text(results.get("reply", "No reply from the chatbot."))
        except Exception as errors:
            await message.reply_text("Failed to decode the chatbot response.")
    elif response.status_code == 429:
        await message.reply_text("ChatBot Error: Too many requests. Please wait a few moments.")
    elif response.status_code >= 500:
        await message.reply_text("ChatBot Error: API server error.")
    else:
        await message.reply_text(f"ChatBot Error: Unknown Error Occurred.")
