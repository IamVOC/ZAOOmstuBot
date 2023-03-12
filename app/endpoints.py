from flask import request


class EndpointActions:

    def __init__(get=None, post=None, put=None, delete=None):
        methods = {
                "GET": get,
                "POST": post,
                "PUT": put,
                "DELETE": delete
                }

    def __call__():
        return methods[request.method](request.json)
