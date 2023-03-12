import requests
from os import environ

def deserialize(json):
    chat_id = json['message']['chat']['id']
    text = json['message']['text']
    return chat_id, text

def main_server_request(message):
    payload = {
            "bot_guid": environ('BOT_GUID'),
            "message": message
            }
    return requests.get(environ('MAIN_SERVER_ADRESS'))
                 
def send_message(payload):
    token = environ('TOKEN')
    url = f'https://api.telegram.org/bot{token}/send_message'
    return requests.post(url, json=payload)

def generate_payload(chat_id, text=None, widgets):
    payload = {
            "parse_mode": "HTML",
            "chat_id": chat_id
            }
    
    if(text):
        payload['text'] = text

    if(widgets):
        payload.update(widgets)

    return payload
