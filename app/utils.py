
@exhandler
def deserialize(json):
    chat_id = json['message']['chat']['id']
    text = json['message']['text']
    return chat_id, text
