import asyncio
from MyTgBot import bot
from pyrogram import filters
from MyTgBot.help.chatsdb import *
from MyTgBot.help.usersdb import *
from pyrogram.enums import ParseMode


@bot.on_message(filters.command(["groupcast","pgroupcast"]))
async def group_cast(_, message):
      if message.from_user.id !=1666544436:
         return await message.reply("`You Don't Have Enough Rights to Do This!`")
      reply = message.reply_to_message
      chat = message.chat  
      if not reply: return await message.reply("Reply to Message to Brodcast!")
      success = "**Group Brodcast**:\n**Success**: `{}`\n**Failed**: `{}`"
      msg = await message.reply("`Please wait Some Minutes!`", quote=True)      
      chat_id = []
      for id in get_chats():
         chat_id.append(id)
      done = 0
      for ids in chat_id:
          try:            
             cast = await bot.copy_message(ids, chat.id, reply.id, parse_mode=ParseMode.DEFAULT)
             if message.text[1].casefold() == "p":
                 try: await cast.pin()
                 except: pass
             done +=1             
             await asyncio.sleep(3)
          except: 
              fail = len(chat_id)-done    
      return await msg.edit(success.format(done, fail))
         
       
@bot.on_message(filters.command(["usercast","pusercast"]))
async def user_cast(_, message):
      if message.from_user.id !=1666544436:
         return await message.reply("`You Don't Have Enough Rights to Do This!`")
      reply = message.reply_to_message
      chat = message.chat  
      if not reply: return await message.reply("Reply to Message to Brodcast!")
      success = "**User Brodcast**:\n**Success**: `{}`\n**Failed**: `{}`"
      msg = await message.reply("`Please wait Some Minutes!`", quote=True)      
      chat_id = []
      for id in get_users():
         chat_id.append(id)
      done = 0
      for ids in chat_id:
          try:
             cast = await bot.copy_message(ids, chat.id, reply.id,parse_mode=ParseMode.DEFAULT)
             done +=1
             if message.text[1].casefold() == "p":
                 try: await cast.pin()
                 except: pass
             await asyncio.sleep(3)
          except: fail = len(chat_id)-done    
      return await msg.edit(success.format(done, fail))
