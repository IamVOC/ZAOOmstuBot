from flask import Flask
from os import environ

class App:
    
    def __init__(self):
        self.app = Flask(__name__)
    
    def run(self, webhook_url):
        self.set_webhook(webhook_url)
        self.app.run(debug=True)
    
    def add_endpoint(self, endpoint=None, endpoint_name=None, EndpointAction):
        self.app.add_url_rule(endpoint, endpoint_name, EndpointAction)

    def set_webhook(self, webhook_url):
        token = environ('TOKEN')
        webhook = f"https://api.telegram.org/bot{token}/setWebhook?url={webhook_url}"
        return requests.get(webhook)
