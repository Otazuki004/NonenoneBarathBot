import requests
import random
from MyTgBot import bot
from pyrogram.types import *
from pyrogram import filters

@bot.on_message(filters.command("mute"))
async def muted(_, message):
      user_id = int(message.from_user.id)
      chat_id = int(message.chat.id)
      mute_id = int(message.text.split(" ")[1])
      reply = message.reply_to_message
      get = await bot.get_chat_member(message.chat.id, message.from_user.id)
      bot_stats = await bot.get_chat_member(chat_id, "self")
      bot_id = bot.me.id
      api = requests.get("https://nekos.best/api/v2/bored").json()
      url = api["results"][0]['url']
      try:
          if not bot_stats.privileges:
                      return await message.reply_text("`Make you sure I'm Admin!`")
                elif mute_id == bot_id:
                      return await message.reply_text("`I can't mute myself!`")
                elif get.privileges:
                      return await message.reply_text("`The User Is Admin! I can't ban!`")
                elif not get.privileges:
                      return await message.reply_text("`Only Admins Can Use This Command`")
                else:
                     await bot.restrict_chat_member(chat_id, mute_id, ChatPermissions(can_send_messages=False))
                     await message.reply_animation(url,caption=f"The Bitch Muted!\n • `{mute_id}`",
                     reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Unmute", callback_data=f"unmute_btn:{mute_id}")]]))
                 else:
                     await message.reply_text("`Your missing the admin rights `can_restrict_members`")
      except Exception as e:
         await message.reply_text(e)
                     


@bot.on_callback_query(filters.regex("unmute_btn"))
async def unmute_btn(_, query):
      chat_id = query.message.chat.id
      user_id = query.from_user.id
      mute_id = query.data.split(":")[1]
      get = await bot.get_chat_member(message.chat.id, message.from_user.id)
      api = requests.get("https://nekos.best/api/v2/smile").json()
      url = api["results"][0]['url']
      try:
          if not get.privileges:
                return await query.answer("Admins Only!")
          else:
             await bot.restrict_chat_member(chat_id, mute_id, ChatPermissions(can_send_messages=True, can_send_media_messages=True, can_send_other_messages=True))
             await query.message.edit_media(media=InputMediaAnimation(url,caption=f"`fine they can speck now!`\nID: `{mute_id}`"))
      except Exception as e:
            await query.message.reply_text(e)
