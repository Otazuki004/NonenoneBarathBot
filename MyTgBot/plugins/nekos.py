from MyTgBot import bot, filters
import requests


@bot.on_message(filters.command("waifu"))
def waifu(_, m):
       reply = m.reply_to_message
       if reply:
           api = requests.get("https://api.waifu.pics/sfw/waifu").json()
           url = api["url"]
           reply.reply_photo(url)
       else:
          api = requests.get("https://api.waifu.pics/sfw/waifu").json()
          url = api["url"]       
          m.reply_photo(photo=url)
