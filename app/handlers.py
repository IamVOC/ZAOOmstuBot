from patterns import Singleton


class MessageHandler(metaclass=Singleton):
    
    def __init__(self):
        self.state = self.default_state 
        self.support = {
                    'CommandHandler': CommandHandler()
                }

    def default_state(self, json):
        chat_id, message = deserialize(json)
        cmhandler = support_objects['CommandHandler']()
        handled, widgets = cmhandler.handle(message)
        if !handled:
            main_server_request(message)
            send_message(generate_payload(chat_id, message))
            return 200, ''
        send_message(generate_payload(chat_id, message, widgets=widgets))
        return 200, ''

    def update_state(self, state, support_objects=None):
        self.state = state
        self.support = support_objects

    def handle(self, json):
        return state(json)

