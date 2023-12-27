from pyrogram import enums
from pyrogram.errors import ChatAdminRequired, RightForbidden, RPCError, UserNotParticipant
from pyrogram import filters
from pyrogram.types import ChatPermissions, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery 
from MyTgBot import bot

@bot.on_message(filters.command(mute))
async def mute(_, m):
    user_id = message.from_user.id
    if not message.reply_to_message:
        await message.reply_text("Give A ID or Reply To A User To Mute!")
        return

    if message.reply_to_message:
      try:
        await message.chat.restrict_member(
            user_id,
            ChatPermissions(),
        )

        await message.reply_text(text= "**Muted {}!**".format(reply.from_user.mention)),
          reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="Unmute", callback_data="unmute"),
                                                    InlineKeyboardButton(text="Delete", callback_data="delete")]])
