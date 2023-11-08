from pyrogram import filters
from pyrogram.types import ChatPermissions
from MyTgBot import bot

@bot.on_message(filters.command("lock"))
async def lock(_, m):
    await bot.set_chat_permissions(m.chat.id, ChatPermissions(can_send_messages=False))
    await reply_and_delete(m, LOCKED)

LOCKED = "Locked successfully!"
UNLOCKED = "Unlocked successfully!"

@bot.on_message(filters.command("unlock"))
async def unlock(_, m):
    await bot.set_chat_permissions(m.chat.id, PERMISSIONS[m.chat.id])
    await reply_and_delete(m, UNLOCKED)

PERMISSIONS = {
    ChatPermissions(
        can_send_messages=True,
        can_send_media_messages=True,
        can_use_inline_bots=True
    )
}
