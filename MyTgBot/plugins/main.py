from pyrogram import filters
from MyTgBot import bot



@bot.on_message(filters.command("start"))
async def start(_, message):
     await message.reply_text("System is alive!")


# you can make this like more commands
@bot.on_message(filters.command("help"))
async def help(_, message):
     await message.reply_text("here is a help")


