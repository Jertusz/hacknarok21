from channels.generic.websocket import AsyncWebsocketConsumer
import json
from channels.auth import channel_session_user_


class SessionConsumer(AsyncWebsocketConsumer):

    async def close(self, code):
        return super().close(code=code)

    @channel_session_user_from_http
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['session_id']
        self.room_group_name = 'chat_%s' % self.room_name

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'exercise_solved',
                'message': message
            }
        )

    async def question_answered(self, event):
        message = event['answer']

        await self.send(text_data=json.dumps({
            'answer': message
        }))
