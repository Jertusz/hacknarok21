from channels.generic.websocket import AsyncWebsocketConsumer
import json
from .models import CustomQuestion, CustomQuestionLog
from channels.db import database_sync_to_async


def add_question_to_db(question):
    question.save()


def get_question(question_id):
    return CustomQuestion.objects.get(pk=question_id)


def add_answer_to_db(answer):
    answer.save()


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

        if event_type == 'activity_question_answered':
            answer = text_data_json['answer']
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': event_type,
                    'answer': answer,
                    'user': self.user_name
                }
            )
        elif event_type == 'custom_question_answered':
            answer = text_data_json['answer']
            question_id = text_data_json['question_id']
            question_from_db = await database_sync_to_async(get_question)(question_id)
            custom_answer_in_db = CustomQuestionLog(session_id=self.session_id, username=self.user_name, answer=answer,
                                                    custom_question=question_from_db)
            await database_sync_to_async(add_answer_to_db)(custom_answer_in_db)
            print(custom_answer_in_db.session_id, custom_answer_in_db.username,
                  custom_answer_in_db.custom_question.content, custom_answer_in_db.answer)

        elif event_type == 'custom_question_asked':
            question = text_data_json['question']
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': event_type,
                    'question': question,
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

    # async def custom_question_answered(self, event):
    #     user = event['user']
    #     answer = event['answer']
    #
    #     await self.send(text_data=json.dumps({
    #         'answer': answer,
    #         'user': user
    #     }))

    async def custom_question_asked(self, event):
        question = event['question']

        question_in_db = CustomQuestion(session_id=self.session_id, content=question)
        await database_sync_to_async(add_question_to_db)(question_in_db)
        await self.send(text_data=json.dumps({
            'question': question,
            'question_id': question_in_db.pk
        }))


