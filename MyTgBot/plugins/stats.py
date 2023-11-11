from pyrogram import filters
from MyTgBot import bot
from MyTgBot.help.usersdb import get_users 
from MyTgBot.help.chatsdb import get_chats


@bot.on_message(filters.command("stats"))
async def stats(_, message):
     if message.from_user.id !=1666544436:
         return await message.reply("`You Don't Have Enough Rights to Do This!`")
     users = len(get_users())
     chats = len(get_chats())
     stats = (
         "**Stats Info:**\n"
         f"**Total Users**: `{users}`\n"
         f"**Total Chats**: `{chats}`")
     await message.reply(stats)
