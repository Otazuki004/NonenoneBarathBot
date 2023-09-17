import asyncio
from pyrogram import filters, Client
from pyrogram.types import ChatJoinRequest
from pyrogram.errors import FloodWait


@bot_client.on_chat_join_request(filters.chat(CHAT))
async def approve(c: Client, m: ChatJoinRequest):
    if not m.from_user:
        return
    try:
        await c.approve_chat_join_request(m.chat.id, m.from_user.id)
    except FloodWait as e:
        logging.info(f"Sleeping for {e.x + 2} seconds due to floodwaits!")
        await asyncio.sleep(e.x + 2)
        await c.approve_chat_join_request(m.chat.id, m.from_user.id)
