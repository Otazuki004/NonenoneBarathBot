from pyrogram import filters
from MyTgBot import app



@app.on_message(filters.command("start"))
async def start(_, message):
     await message.reply_text("Your Start message Text")


# you can make this like more commands
@app.on_message(filters.command("help"))
async def help(_, message):
     await message.reply_text("Your help Text")


