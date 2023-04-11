from MyTgBot import bot
import config


if __name__ == "__main__":
    bot.run()
    with bot:
       bot.send_message(
            config.GROUP_ID, 
            text="Bot started!")
