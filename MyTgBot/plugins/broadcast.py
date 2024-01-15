import asyncio

from pyrogram import filters
from pyrogram.errors import FloodWait

from MyTgBot import bot
from MyTgBot.database import *

@bot.on_message(filters.command("broadcast"))
async def broadcast(_, m):
    if m.reply_to_message:
        x = m.reply_to_message.message.id
        y = m.chat.id
    else:
        if len(m.command) < 2:
            return await m.reply_text(
                "**Usage**:\n/broadcast [MESSAGE] or [Reply to a Message]"
            )
        query = m.text.split(None, 1)[1]
    sent = 0
    chats = []
    schats = await get_served_chats()
    for chat in schats:
        chats.append(int(chat["chat_id"]))
    for i in chats:
        try:
            await bot.forward_messages(
                i, y, x
            ) if m.reply_to_message else await bot.send_message(
                i, text=query
            )
            sent += 1
        except FloodWait as e:
            flood_time = int(e.x)
            if flood_time > 200:
                continue
            await asyncio.sleep(flood_time)
        except Exception:
            continue
    try:
        await m.reply_text(
            f"**Broadcasted Message In {sent} Chats.**"
        )
    except:
        pass
