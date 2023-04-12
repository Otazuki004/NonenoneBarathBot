from pyrogram import filters
from pyrogram.types import Message
from pyrogram.types.bots_and_keyboards.inline_keyboard_button import InlineKeyboardButton
from pyrogram.types.bots_and_keyboards.inline_keyboard_markup import InlineKeyboardMarkup
from pyrogram.types import CallbackQuery
from MyTgBot import bot

START_TEXT = """
I Already Awake!  ( • ̀ω•́  )!

• Read the help menu for about my futures /help.
"""

@bot.on_message(filters.command("start"))
async def start(_, message):
     await message.reply_text(START_TEXT),
     reply_markup=(buttons))

    buttons = [
        [
            InlineKeyboardButton(
                "ADD ME", url="t.me/cuteserenabot?startgroup=true"),
            InlineKeyboardButton(
                "HELP", callback_data='help_back'),]]


@bot.on_message(filters.command("help"))
async def help(_, message):
     await message.reply_text(HELP_TEXT),
     reply_markup=(HELP_BUTTON))
     

HELP_TEXT = """
Click the button below to know my commands!
"""

HELP_BUTTON = [[
        InlineKeyboardButton('Admin', callback_data='admin_help'),
        InlineKeyboardButton('UserInfo', callback_data='userinfo_help'),
        InlineKeyboardButton('Fun', callback_data='fun_help'),
        InlineKeyboardButton('Misc', callback_data='misc_help'),
        InlineKeyboardButton('Tagging', callback_data='tagging_help')]]

@bot.on_callback_query(filters.regex("help_back"))
async def help(_, query: CallbackQuery):
    await query.message.edit_caption(HELP_TEXT,
                                    reply_markup=(HELP_BUTTON))

@bot.on_callback_query(filters.regex("close"))
async def close(_, query: CallbackQuery):
           query = query.message
           await query.delete()


ADMIN_TEXT = """
Usage of admin commands:
• /promote - promote a user.
• /demote - demote a user.
• /pin - pin a message
• /unpin - unpin a message
• /del - delete a message
• /setgpic - set group pic.
• /setgtitle - set group title.
"""

@bot.on_callback_query(filters.regex("admin_help"))
async def adminhelp(_, query: CallbackQuery):
     await query.message.edit_caption(ADMIN_TEXT,
                                      reply_markup=(BUTTON))

USERINFO_TEXT = """
User info:
• /id - userid & chatid.
• /info - user information.
"""

@bot.on_callback_query(filters.regex("userinfo_help"))
async def userinfohelp(_, query: CallbackQuery):
     await query.message.edit_caption(USERINFO_TEXT,
                                      reply_markup=(BUTTON))
MICS_TEXT = """
Extra commands:
• /tm - reply media to get telegraph link.
• /txt - reply text with suitable name and get telegraph text link.
• /tr - reply text to translate the message.
• /write - to write a message.
"""

@bot.on_callback_query(filters.regex("mics_help"))
async def micshelp(_, query: CallbackQuery):
     await query.message.edit_caption(MICS_TEXT,
                                      reply_markup=(BUTTON))
TAGGING_TEXT = """
Tagging a group members:
• /tagall - tag a group members.
• /stop - stop tagging.
"""

@bot.on_callback_query(filters.regex("tagging_help"))
async def tagginghelp(_, query: CallbackQuery):
     await query.message.edit_caption(TAGGING_TEXT,
                                      reply_markup=(BUTTON))
FUN_TEXT = """
Usage of fun commands:
• /react - react a message.
• /aq - random sent animequotes.
• /dice - sent a dice
• /truth - sent a truth message.
• /dare - sent a dare message.
"""

@bot.on_callback_query(filters.regex("fun_help"))
async def funhelp(_, query: CallbackQuery):
     await query.message.edit_caption(FUN_TEXT,
                                      reply_markup=(BUTTON)) 


