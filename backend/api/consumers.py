from channels.generic.websocket import AsyncWebsocketConsumer
import json
import random
from .models import CustomQuestion, CustomQuestionLog, Question, ActivityLog, SessionLog, Log
from channels.db import database_sync_to_async


def add_question_to_db(question):
    question.save()


def get_question(question_id):
    return CustomQuestion.objects.get(pk=question_id)


def add_answer_to_db(answer):
    answer.save()


def get_random_question(session_id):
    questions = Question.objects.values_list('pk', flat=True)
    random_pk = random.choice(questions)
    session = SessionLog.objects.get(session_id=session_id)
    random_question = Question.objects.get(pk=random_pk)
    new_activity_question = ActivityLog(session_id=session, no_answer=session.users, question=random_question)
    new_activity_question.save()

    return new_activity_question


def generic_log(username, session_id, action, text):
    session_in_db = SessionLog.objects.get(session_id=session_id)
    log = Log(session_id=session_in_db, action=action, text=text, student=username)
    log.save()


def create_or_update_session(session_id, username, is_admin):
    if not SessionLog.objects.filter(session_id=session_id).exists():
        if is_admin == "True":
            new_session = SessionLog(session_id=session_id, admin=username)
            new_session.save()
    else:
        if is_admin == "False":
            session_in_db = SessionLog.objects.get(session_id=session_id)
            session_in_db.users.append(username)
            session_in_db.save()


def activity_answered(username, question, answer):
    activity_question = ActivityLog.objects.get(pk=question)
    if activity_question.question.right_answer == answer:
        activity_question.answered_right.append(username)
    else:
        activity_question.answered_wrong.append(username)
    activity_question.no_answer.remove(username)
    activity_question.save()


class SessionConsumer(AsyncWebsocketConsumer):

    async def close(self, code):
        return super().close(code=code)

    async def connect(self):
        self.session_id = self.scope['url_route']['kwargs']['session_id']
        self.user_name = self.scope['url_route']['kwargs']['username']
        self.is_admin = self.scope['url_route']['kwargs']['admin']
        self.room_group_name = 'session_%s' % self.session_id

        await database_sync_to_async(create_or_update_session)(self.session_id, self.user_name, self.is_admin)

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
            question_id = text_data_json['question_id']
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': event_type,
                    'answer': answer,
                    'question_id': question_id,
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
                  custom_answer_in_db.custom_question.content, custom_answer_in_db.answer, custom_answer_in_db.pk)

        elif event_type == 'custom_question_asked':
            question = text_data_json['question']
            if self.is_admin:
                question_in_db = CustomQuestion(session_id=self.session_id, content=question)
                await database_sync_to_async(add_question_to_db)(question_in_db)
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': event_type,
                    'question': question,
                    'question_id': question_in_db.pk
                }
            )

        elif event_type == 'show_activity_question':
            if self.is_admin:
                question = await database_sync_to_async(get_random_question)(self.session_id)
                await self.channel_layer.group_send(
                    self.room_group_name,
                    {
                        'type': event_type,
                        'question': question.question.content,
                        'question_id': question.pk,
                    }
                )
        elif event_type == 'hide':
            if self.is_admin:
                await self.channel_layer.group_send(
                    self.room_group_name,
                    {
                        'type': event_type,
                    }
                )

        elif event_type == 'generic':
            action = text_data_json['action']
            text = text_data_json['text']
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': event_type,
                    'action': action,
                    'text': text,
                }
            )

    async def show_activity_question(self, event):
        question = event["question"]
        question_id = event["question_id"]
        await self.send(text_data=json.dumps({
            'question': question,
            'question_id': question_id,
        }))

    async def activity_question_answered(self, event):
        question = event["question_id"]
        answer = event["answer"]
        await database_sync_to_async(activity_answered)(self.user_name, question, answer)

    async def custom_question_asked(self, event):
        question = event['question']
        question_id = event['question_id']

        await self.send(text_data=json.dumps({
            'question': question,
            'question_id': question_id
        }))

    async def hide(self):
        await self.send(text_data=json.dumps({
            'message': 'hide',
        }))

    async def generic(self, event):
        action = event['action']
        text = event['text']
        await database_sync_to_async(generic_log)(self.user_name, self.session_id, action, text)
        await self.send(text_data=json.dumps({
            'username': self.user_name,
            'action': action,
            'text': text,
        }))
