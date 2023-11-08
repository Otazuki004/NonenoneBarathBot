from asyncio import sleep
from pyrogram import filters
from pyrogram.types import ChatPermissions
from MyTgBot import bot

@bot.on_message(filters.command("lock"))
async def lock(_, m):
    if not get.privileges:
       return await message.reply("-› Sorry, **only admins** can execute this command!")
       await bot.set_chat_permissions(m.chat.id, ChatPermissions(can_send_messages=False))
       lock = await m.reply_text(LOCKED)
       await sleep(10)
       await lock.delete()
  except Exception as errors:
           await message.reply(f"**Error**: {errors}")

LOCKED = "Locked successfully!"
UNLOCKED = "Unlocked successfully!"

@bot.on_message(filters.command("unlock"))
async def unlock(_, m):
    if not get.privileges:
       return await message.reply("-› Sorry, **only admins** can execute this command!")
       await bot.set_chat_permissions(m.chat.id, PERMISSIONS[m.chat.id])
       unlock = await m.reply_text(UNLOCKED)
       await sleep(10)
       await unlock.delete()
   except Exception as errors:
           await message.reply(f"**Error**: {errors}")

PERMISSIONS = ChatPermissions(
        can_send_messages=True,
        can_send_media_messages=True
)
