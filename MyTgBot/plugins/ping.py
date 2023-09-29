import time
from pyrogram import filters

from MyTgBot import bot, start, version
from MyTgBot.help.readable_time import get_readable_time


@bot.on_message(filters.command("ping"))
async def ping(_, message):
    currentTime = get_readable_time(time.time() - start)
    start_t = time.time()
    rm = await message.reply_photo("https://telegra.ph/file/3f7514ba939b5df5862da.jpg", caption="Pong..")
    end_t = time.time()
    time_taken_s = round(end_t - start_t, 3)
    await rm.edit_caption(
        f"""
**BOT VERSION:** {version}

**PING:** {time_taken_s} seconds
**UPTIME:** {currentTime}"""
    )
