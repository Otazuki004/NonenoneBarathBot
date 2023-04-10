import re
import requests
import random

from MyTgBot import bot
from pyrogram import filters


GM_TEXT = [
"Let your morning be the start of your new life. Do your best and forget about the rest. Good morning!",
"Good morning, wake up. Start fresh and see the beautiful opportunity in each day. Wish you all the very best!",
"Whenever you find yourself in doubt about how far you can go, just remember how far you have come. Stay positive and always have faith in yourself. Good morning!",
"Keep moving on in life. Everything you need will come to you at a perfect time. Just believe in yourself and keep doing hard work. Good morning!",
"Good morning sunshine, waking up with your beautiful smile makes my day extraordinary.",
"Good morning to the beautiful soul, your positive energy makes me enthusiastic, thank you, love!",
"Can't wait for the day when you wake up next to me, good morning sweetheart!",
"Good morning to my world, may you have a positive day and find solutions to all your problems.",
"It's the best morning when you wake up next to me, good morning love!",
"Good morning darling, the warmth of your hugs and love makes me special every day!",
"I don't need an alarm when I have you, you are my snooze-buster. Good morning love!",]

GN_TEXT = [
"I hope God blesses you with many more peaceful nights. Good night, dear.",
"When your day gets tough, remember that tomorrow is a fresh day after your sleep. Good night.",
"Good night, my one and only. I wish I could hold you in my arms right now as I go to sleep.",
"May the stars and moonlight shine brightly on your night. Have a good night.",
"Have a good night, friend. May you have a restful and pleasant night’s sleep tonight.",
"No matter how bad the day was, always try to end it with positive thoughts. Try to focus on the next day and hope for a sweet dream. Good night.",
"You have so many reasons to thank God, but first thank him for such a peaceful night like this. What a blissful night for a good sleep. Good night!",
"I don’t need anything else to warm me up as long as you love me. Because the warmth of your love is all I need. Good night!",
"Do you know when an ordinary dream becomes a sweet dream? When someone as sweet as you is present in it. Good night! Please come and make my dreams sweeter!",
"Good night dear. Tomorrow, you are going to have a great day. Just make sure your body is prepared to take on the challenges of tomorrow. Sleep well!",
"A new morning is waiting for you. Sleep well and sleep tight. Because the new day wants you to be fit and all charged up. Good night!",]

GE_TEXT = [
"Evenings allow you to forget the bitter worries of the day and get ready for the sweet dreams of night. Evenings give you relaxation from a stressful day. Good evening!",
"A very good evening to you. Just wish that you have a good time. Let the fun begin with that super wide grin. Have a great time. Good evening!",
"Stay happy and the situation will also turn happy, stay positive and keep smiling, and always stay in bliss. Good evening!",
"Evenings are great not because it is the coolest time of the day, but because it lets you reflect on your whole day and forget your yesterday. Good evening!",
"Sunsets are amazing, hope you are enjoying your evening perfectly!",
"Good evening, hope you had a wonderful day and may you have a celebratory night!",
"Take a look at the sunset and see the beautiful colors of life, good evening!",
"Some days are going to be tough, some are going to be good but you have to keep your head strong and believe in yourself. Good evening!",
"Every day brings unknown opportunities and challenges. But it ends with a peaceful evening. Hope you are enjoying this evening after a rewarding day. Good Evening dear friend!",
"I miss your presence every evening. Our hot cup of coffee, long talks and game of chess. Miss you a lot, good evening.",
"From morning till evening, life is full of momentous moments. Have a happy evening!",
"The evening is a pause button of a hectic day. Enjoy the time and get ready for the another today. Good Evening.",
]

GA_TEXT = [
"Good afternoon, enjoy this amazing afternoon. I cherish and love you so much.",
"You mean the entire world to me, sweetheart; enjoy your afternoon.",
"I miss you a lot, dear. I hope you are here with me this beautiful afternoon. Blessed afternoon.",
"Even though distance has kept you away from me this afternoon, I hope you have a lovely afternoon. I love you.",
"You are a God-given gem to me. Very rare, unique, and I will forever treasure you. Enjoy your afternoon, darling.",
"I miss every moment we sit and share our thoughts and our feelings. Good afternoon my king.",
"This afternoon sunshine keeps triggering the thoughts of having you. Your love towards me enlightens me and gives me a reason to yearn for tomorrow. Good afternoon handsome.",
"How I hope you have a refreshing afternoon. Take a deep breath, and you will smell the love I have for you in the air. I give you my whole heart, love you.",
"I can’t wait to have you in my arms this evening. Have a beautiful afternoon and come to me as soon as possible.",
"My dear friend, like the water, evaporates in the sun; your gloomy days will soon disappear. Keep up the good work and give your best.",
"There is nothing like coincidences or mistakes; everything that happens in our lives is a blessing. It is a stepping stone to a much longer journey. Enjoy your afternoon, my dear friend.",
"How I wish you could spend the whole day with me, but your dreams are the priority for both of us. However, after you have completed it, I will always be waiting for you. Have a beautiful afternoon.",]

@bot.on_message(filters.regex("morning|night|evening|afternoon"))
async def mornings(_, message):
        if re.search("morning", message.text):
                 return await message.reply(text="**yee? {} good morning! and for you my quote 🥰**\n`{}`".format(message.from_user.first_name, random.choice(GM_TEXT)))
        elif re.search("night", message.text):
                 return await message.reply(text="**yee? {} good night! and for you my quote 🥰**\n`{}`".format(message.from_user.first_name, random.choice(GN_TEXT)))
        elif re.search("evening", message.text):
                 return await message.reply(text="**yee? {} good evening! and for you my quote 🥰**\n`{}`".format(message.from_user.first_name, random.choice(GE_TEXT)))
        elif re.search("afternoon", message.text):
                 return await message.reply(text="**yee? {} good afternoon! and for you my quote 🥰**\n`{}`".format(message.from_user.first_name, random.choice(GA_TEXT)))
