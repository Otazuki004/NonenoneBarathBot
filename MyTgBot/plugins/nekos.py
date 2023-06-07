from MyTgBot import bot
from pyrogram import filters
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

       
@bot.on_message(filters.command("cuddle"))
def cuddle(_, m):
      reply = m.reply_to_message
      if reply:
          api = requests.get("https://nekos.best/api/v2/cuddle").json()
          url = api["results"][0]['url']
          reply.reply_animation(url)
      else:
          api = requests.get("https://nekos.best/api/v2/cuddle").json()
          url = api["results"][0]['url']
          m.reply_animation(animation=url)
              
              
@bot.on_message(filters.command("neko"))
def neko(_, m):
      reply = m.reply_to_message
      if reply:
          api = requests.get("https://nekos.best/api/v2/neko").json()
          url = api["results"][0]['url']
          reply.reply_photo(url)
      else:
          api = requests.get("https://nekos.best/api/v2/neko").json()
          url = api["results"][0]['url']
          m.reply_photo(url)
              
              
@bot.on_message(filters.command("dance"))
def dance(_, m):
      reply = m.reply_to_message
      if reply:
          api = requests.get("https://nekos.best/api/v2/dance").json()
          url = api["results"][0]['url']
          reply.reply_animation(url)
      else:
          api = requests.get("https://nekos.best/api/v2/dance").json()
          url = api["results"][0]['url']
          m.reply_animation(animation=url)
              

@bot.on_message(filters.command("baka"))
def baka(_, m):
      reply = m.reply_to_message
      if reply:
          api = requests.get("https://nekos.best/api/v2/baka").json()
          url = api["results"][0]['url']
          reply.reply_animation(url)
      else:
          api = requests.get("https://nekos.best/api/v2/baka").json()
          url = api["results"][0]['url']
          m.reply_animation(animation=url)
              

@bot.on_message(filters.command("bore"))
def bore(_, m):
      reply = m.reply_to_message
      if reply:
          api = requests.get("https://nekos.best/api/v2/bored").json()
          url = api["results"][0]['url']
          reply.reply_animation(url)
      else:
          api = requests.get("https://nekos.best/api/v2/bored").json()
          url = api["results"][0]['url']
          m.reply_animation(animation=url)


@bot.on_message(filters.command("laugh"))
def laugh(_, m):
      reply = m.reply_to_message
      if reply:
          api = requests.get("https://nekos.best/api/v2/laugh").json()
          url = api["results"][0]['url']
          reply.reply_animation(url)
      else:
          api = requests.get("https://nekos.best/api/v2/laugh").json()
          url = api["results"][0]['url']
          m.reply_animation(animation=url)
              
              
@bot.on_message(filters.command("sleep"))
def sleep(_, m):
      reply = m.reply_to_message
      if reply:
          api = requests.get("https://nekos.best/api/v2/sleep").json()
          url = api["results"][0]['url']
          reply.reply_animation(url)
      else:
          api = requests.get("https://nekos.best/api/v2/sleep").json()
          url = api["results"][0]['url']
          m.reply_animation(animation=url)
              
              
@bot.on_message(filters.command("cry"))
def cry(_, m):
       reply = m.reply_to_message
       if reply:
           api = requests.get("https://api.waifu.pics/sfw/cry").json()
           url = api["url"]
           reply.reply_animation(url)
       else:
          api = requests.get("https://api.waifu.pics/sfw/cry").json()
          url = api["url"]
          m.reply_animation(animation=url)
       
       
@bot.on_message(filters.command("kill"))
def kill(_, m):
       reply = m.reply_to_message
       if reply:
           api = requests.get("https://api.waifu.pics/sfw/kill").json()
           url = api["url"]
           reply.reply_animation(url)
       else:
          api = requests.get("https://api.waifu.pics/sfw/kill").json()
          url = api["url"]
          m.reply_animation(animation=url)       
