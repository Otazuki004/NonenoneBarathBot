from pyrogram import filters
from MyTgBot import bot

START_TEXT = """
I Already Awake!  ( • ̀ω•́  )!

• Read the help menu for about my futures /help.
"""

@bot.on_message(filters.command("start"))
async def start(_, message):
     await message.reply_text(START_TEXT)


# you can make this like more commands
@bot.on_message(filters.command("help"))
async def help(_, message):
     await message.reply_text("Click button below to know my commands")


