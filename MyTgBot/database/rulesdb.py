from MyTgBot import mongodb

rulesdb = mongodb.RULES 


def rules_chat():
    chats = []
    for chat_id in rulesdb.find():
         chats.append(chat_id["_id"])
    return chats

def get_rules(chat_id: int):
     if not chat_id in rules_chat():
         return
     x = rulesdb.find_one({"_id": chat_id})
     return x["rules"]
           

def add_rules(chat_id: int, text: str):
    RULES = {"_id": chat_id, "rules": text}
    if chat_id in rules_chat():
        return
    return rulesdb.insert_one(RULES)

def remove_rules(chat_id: int):
    if not chat_id in rules_chat():
        return
    x = rulesdb.find_one({"_id": chat_id})
    rulesdb.delete_one(x)

def update_rules(chat_id: int, text: str):
      if not chat_id in rules_chat():
         return
      rulesdb.update_one({"_id": chat_id},{"$set":{"rules":text}})
