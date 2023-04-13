from MyTgBot import bot
import config

if __name__ == "__main__":
    bot.run()
    with bot:
       bot.send_sticker(config.GROUP_ID, sticker="CAACAgQAAx0CatX7ugAC1Q5je29sMbWkm8pX9KFL-LgW5MScSgACXgEAAiIN2QABm8LQQ_qSuqceBA")
