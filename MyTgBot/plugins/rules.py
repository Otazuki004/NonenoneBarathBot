from MyTgBot import bot
from MyTgBot.database.rulesdb import *
from pyrogram import filters
from pyrogram import enums
from pyrogram.types import *


@bot.on_message(filters.command("setrules"))
async def setrules(_, message):
   chat_id = message.chat.id
   user_id = message.from_user.id
   reply = message.reply_to_message
   get = await bot.get_chat_member(message.chat.id, message.from_user.id)
   if message.chat.type == enums.ChatType.PRIVATE:
        return message.reply("try on groups not in dms",quote=True)
   if not get.privileges:
        return await message.reply("`Admins Only!`")
   else:
        if reply and (reply.text or reply.caption):
            RULES = reply.text or reply.caption
        elif not reply and len(message.text.split()) <2:
            return await message.reply("`reply to text message or give text to set rules!`")
        elif not reply and len(message.text.split()) >1:
             RULES = message.text.replace(message.text.split()[0], "")
        if chat_id in rules_chat():
                 update_rules(chat_id,RULES)
                 await message.reply("`Group Rules already set so I have updated the Rules Successfully!`")
        else:
                 add_rules(chat_id,RULES)
                 await message.reply("`Group Rules set Successfully!`")
             
              
@bot.on_message(filters.command("rules"))
async def rules(_, message):
    chat_id = int(message.chat.id)
    reply = message.reply_to_message
    if message.chat.type == enums.ChatType.PRIVATE:
        return await message.reply("try on groups not in dms",quote=True)
    else: 
       if reply and chat_id in rules_chat():
          return await message.reply_to_message.reply_text("click below button to get rules in this chat!",
           reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Rules" , url=f"https://t.me/cuteserenabot?start=rules{chat_id}")]]))
       elif not reply and chat_id in rules_chat(): 
          return await message.reply_text("click below button to get rules in this chat!",
           reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Rules" , url=f"https://t.me/cuteserenabot?start=rules{chat_id}")]]))
       else: return await message.reply_text("Semms Like This Chat Don't Haven't Any Rules!")

    
    
@bot.on_message(filters.command(["removerules","clearrules"]))
async def remove(_, message):
     chat_id = message.chat.id
     user_id = message.from_user.id
     get = await bot.get_chat_member(message.chat.id, message.from_user.id)
     if message.chat.type == enums.ChatType.PRIVATE:
         return message.reply("try on groups not in dms",quote=True)
     if not get.privileges:
           return await message.reply("`Admins only!`")
     else:
         if not chat_id in rules_chat():
              return await message.reply("`This Chat Don't haven't Any Rules!`")
         else:
             remove_rules(chat_id)
             await message.reply("`Successfully Rules Removed!`")
