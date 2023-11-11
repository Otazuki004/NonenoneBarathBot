from Nandha import mongodb

chatbotdb = mongodb.CHATBOT 


def get_chat():
     chats = []
     for chat_ids in chatbotdb.find():
          chats.append(chat_ids["chat_id"])
     return chats

def addchat(chat_id: int):
    if chat_id in get_chat():
      return
    return chatbotdb.insert_one({"chat_id": chat_id})

def removechat(chat_id: int):
    x = chatbotdb.find_one({"chat_id": chat_id})  
    chatbotdb.delete_one(x)

def is_chat(chat_id: int):
     x = chatbotdb.find_one({"chat_id": chat_id}) 
     if x:
        return True
     return False 

