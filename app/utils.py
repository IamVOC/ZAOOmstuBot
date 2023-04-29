import requests
from decouple import config


def deserialize(json_req):
    chat_id = json_req['message']['chat']['id']
    text = json_req['message']['text']
    return chat_id, text


def main_server_request(chat_id, message):
    payload = {
        "bot_guid": config('BOT_GUID'),
        "message": message,
        "client_id": chat_id
    }
    return requests.post(config('MAIN_SERVER_ADDRESS'), json=payload)


def send_message(payload):
    token = config('TOKEN')
    url = f'https://api.telegram.org/bot{token}/sendMessage'
    return requests.post(url, json=payload)


def generate_payload(chat_id, text=None, widgets=None):
    payload = {
        "parse_mode": "HTML",
        "chat_id": chat_id
    }

    if (text):
        payload['text'] = text

    return payload
