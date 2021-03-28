# Generated by Django 3.1.7 on 2021-03-27 17:56

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CustomQuestion",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("session_id", models.CharField(max_length=255)),
                ("content", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Log",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("GD", "Good"),
                            ("BD", "Bad"),
                            ("NN", "None"),
                            ("NT", "Neutral"),
                        ],
                        max_length=255,
                    ),
                ),
                (
                    "action",
                    models.CharField(
                        choices=[
                            ("CC", "Change Card"),
                            ("SE", "Session Enrollment Change"),
                            ("CW", "Clicked Different Window"),
                            ("AQ", "Answered Question"),
                        ],
                        max_length=255,
                    ),
                ),
                ("text", models.CharField(max_length=255)),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("student", models.CharField(max_length=255)),
            ],
            options={
                "verbose_name": "log",
                "verbose_name_plural": "logs",
            },
        ),
        migrations.CreateModel(
            name="Question",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("content", models.CharField(max_length=255)),
                ("right_answer", models.CharField(max_length=255)),
            ],
            options={
                "verbose_name": "question",
                "verbose_name_plural": "questions",
            },
        ),
        migrations.CreateModel(
            name="CustomQuestionLog",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("session_id", models.CharField(max_length=255)),
                ("username", models.CharField(max_length=255)),
                ("answer", models.CharField(max_length=255)),
                (
                    "custom_question",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="api.customquestion",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ActivityLog",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("session_id", models.CharField(max_length=255)),
                (
                    "answered_right",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.CharField(max_length=255), size=None
                    ),
                ),
                (
                    "no_answer",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.CharField(max_length=255), size=None
                    ),
                ),
                (
                    "answered_wrong",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.CharField(max_length=255), size=None
                    ),
                ),
                (
                    "question",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="api.question"
                    ),
                ),
            ],
            options={
                "verbose_name": "activitylog",
                "verbose_name_plural": "activitylogs",
            },
        ),
    ]