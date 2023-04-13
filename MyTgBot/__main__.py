from MyTgBot import bot

if __name__ == "__main__":
    bot.run()
    with bot:
       bot.send_message(
            -1001785150977, 
            text="Bot started!")
