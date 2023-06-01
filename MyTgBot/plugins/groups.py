from pyrogram import filters
from MyTgBot import bot
from pyrogram.types import *
from pyrogram.enums import ChatType


@bot.on_message(filters.new_chat_members)
async def new_chat(_, message):
    chat = str(message.chat.id).replace("-100", "")
    bot_id = (await bot.get_me()).id
    await add_group(chat)
    for member in message.new_chat_members:
        if member.id == bot_id:
            await message.reply(
                "😘 Thanks for add me to your group!"
            )
