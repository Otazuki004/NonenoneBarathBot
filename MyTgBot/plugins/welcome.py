from pyrogram import filters
from pyrogram.types import Message
from MyTgBot import bot

WEL_GIF = "https://telegra.ph/file/b616d3a126715d9b1aa46.mp4"

@bot.on_message(filters.new_chat_members)
async def welcome(_, m: Message):
        await m.reply_animation(WEL_GIF,caption="hello! dear {}\nWelcome **{}**!".format(m.from_user.mention,m.chat.title))
        
@bot.on_message(filters.left_chat_member)
async def member_has_left(_, m: Message):
        await m.reply("oof! dear {}\nlefted **{}**".format(m.from_user.mention,m.chat.title))
