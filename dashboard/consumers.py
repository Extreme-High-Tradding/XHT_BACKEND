from channels.generic.websocket import WebsocketConsumer, JsonWebsocketConsumer

class BalanceConsumer(WebsocketConsumer):
    pass

class AssetsConsumer(JsonWebsocketConsumer):
    # Here code the API trading data handling
    pass

