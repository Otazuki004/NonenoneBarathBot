from pyrogram import filters
from MyTgBot import bot
from pyrogram.types import *
import requests




@app.on_message(filters.command("dice"))
async def roll_dice(bot, message):
    await bot.send_dice(message.chat.id, "🎲")

@app.on_message(filters.command(["dart","arrow"]))                                     
async def roll_arrow(bot, message):
    await bot.roll_arrow(message.chat.id, "🎯")

@app.on_message(filters.command(["football","goal"]))
async def roll_goal(bot, message):
    await bot.roll_goal(message.chat.id, "⚽️")

@app.on_message(filters.command("roll"))
async def roll_luck(bot, message):
    await bot.roll_luck(message.chat.id, "🎰")

@app.on_message(filters.command(["throw","basket"]))
async def roll_throw(bot, message):
    await bot.roll_throw(message.chat.id, "🏀")



#Truth OR Dare Game

@app.on_message(filters.command("dare"))
async def dare(_, m):
         reply = m.reply_to_message
         if reply:
               api = requests.get("https://api.truthordarebot.xyz/v1/dare").json()
               text = api["question"]
               dare = f"""
**Hey! {reply.from_user.mention}
{m.from_user.mention} give you a dare!
Dare**: `{text}`
               """
               await m.reply_text(dare)
         else:
               api = requests.get("https://api.truthordarebot.xyz/v1/dare").json()
               text = api["question"]
               dare = f"""
 Hey! {m.from_user.mention} your dare here!
 **Dare**: `{text}`
               """
               await m.reply_text(dare)

@app.on_message(filters.command("truth"))
async def truth(_, m):
         reply = m.reply_to_message
         if reply:
               api = requests.get("https://api.truthordarebot.xyz/v1/truth").json()
               text = api["question"]
               truth = f"""
  Hey! {reply.from_user.mention}
  {m.from_user.mention} give you a Truth!
  **Truth**: `{text}`
               """
               await m.reply_text(truth)
         else:
               api = requests.get("https://api.truthordarebot.xyz/v1/Truth").json()
               text = api["question"]
               truth = f"""
    Hey! {m.from_user.mention} your Truth here!
    **Truth**: `{text}`
               """
               await m.reply_text(truth)
