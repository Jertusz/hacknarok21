from channels.generic.websocket import AsyncWebsocketConsumer


class SessionConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        return super().connect()

    async def close(self, code):
        return super().close(code=code)

    async def receive(self, text_data, bytes_data):
        return super().receive(text_data=text_data, bytes_data=bytes_data)

    async def receive(self, text_data, bytes_data):
        return super().receive(text_data=text_data, bytes_data=bytes_data)