from MyTgBot import bot
from pyrogram import enums


async def is_admin(chat_id: int, user_id: int):
     admin = await bot.get_chat_member(chat_id, user_id)
     if admin.privileges:
         return True
     return False


async def can_ban_members(chat_id: int, user_id: int):
     admin = await bot.get_chat_member(chat_id, user_id)
     if admin.privileges.can_restrict_members:
         return True
     return False
