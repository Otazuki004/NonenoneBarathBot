import asyncio
from MyTgBot import bot
from pyrogram import filters
from pyrogram.types import ChatJoinRequest
from pyrogram.errors import FloodWait


@bot.on_chat_join_request(filters.group | filters.channel)
async def approve(_, m: ChatJoinRequest):
    if not m.from_user:
        return
    try:
        await bot.approve_chat_join_request(m.chat.id, m.from_user.id)
    except FloodWait as e:
        logging.info(f"Sleeping for {e.x + 2} seconds due to floodwaits!")
        await asyncio.sleep(e.x + 2)
        await bot.approve_chat_join_request(m.chat.id, m.from_user.id)
