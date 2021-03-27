from channels.generic.websocket import AsyncWebsocketConsumer
import json


class SessionConsumer(AsyncWebsocketConsumer):

    async def close(self, code):
        return super().close(code=code)

    async def connect(self):
        self.session_id = self.scope['url_route']['kwargs']['session_id']
        self.user_name = self.scope['url_route']['kwargs']['username']
        self.is_admin = self.scope['url_route']['kwargs']['admin']
        self.room_group_name = 'session_%s' % self.session_id

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
        event_type = text_data_json['type']

        if event_type == 'question_answered':
            answer = text_data_json['answer']
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': event_type,
                    'answer': answer,
                    'user': self.user_name
                }
            )
        elif event_type == 'question_asked':
            question = text_data_json['question']
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': event_type,
                    'question': question,
                    'user': self.user_name
                }
            )
        elif event_type == 'show_activity_question':
            if self.is_admin:
                question = text_data_json['question']
                await self.channel_layer.group_send(
                    self.room_group_name,
                    {
                        'type': event_type,
                        'question': question,
                    }
                )
        elif event_type == 'hide_activity_question':
            if self.is_admin:
                await self.channel_layer.group_send(
                    self.room_group_name,
                    {
                        'type': event_type,
                        'message': 'hide',
                    }
                )

    async def question_answered(self, event):
        user = event['user']
        answer = event['answer']

        await self.send(text_data=json.dumps({
            'answer': answer,
            'user': user
        }))

    async def question_asked(self, event):
        question = event['question']

        await self.send(text_data=json.dumps({
            'question': question
        }))
