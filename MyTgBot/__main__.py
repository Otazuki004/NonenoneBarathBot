from MyTgBot import app


if __name__ == "__main__":
    app.run()
    with app:
       app.send_message(
            chat_id=GROUP_ID, 
            text="Am I Restarted!")
