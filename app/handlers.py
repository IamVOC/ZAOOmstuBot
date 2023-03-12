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
            predicted_message = main_server_request(message)
            send_message(generate_payload(chat_id, predicted_message))
            return 200, ''
        send_message(generate_payload(chat_id, handled, widgets=widgets))
        return 200, ''

    def update_state(self, state, support_objects=None):
        self.state = state
        self.support = support_objects

    def handle(self, json):
        return state(json)
   


class CommandHandler:

    def __init__(self):
        self.command_dicts = {
                '/start': self.default_start_command
                }

    def default_start_command():
        return "<b>ZAO bot</b> - это бот в котором вы наверняка сможете найти ответ на ваш вопрос по заочному образованию. Если вы хотите получить ответ, то просто напишите мне нужный вопрос", None

    def change_commands(self, command, action):
        self.command_dicts[command] = action

    def handle(self, message):
        if message in self.command_dicts:
            return command_dicts[message]
        return None, None

