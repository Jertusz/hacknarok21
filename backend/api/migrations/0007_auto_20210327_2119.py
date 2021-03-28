# Generated by Django 3.1.7 on 2021-03-27 21:19

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0006_auto_20210327_1946"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="log",
            name="status",
        ),
        migrations.AlterField(
            model_name="activitylog",
            name="answered_right",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.CharField(max_length=255), default=list, size=None
            ),
        ),
        migrations.AlterField(
            model_name="activitylog",
            name="answered_wrong",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.CharField(max_length=255), default=list, size=None
            ),
        ),
        migrations.AlterField(
            model_name="activitylog",
            name="no_answer",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.CharField(max_length=255), default=list, size=None
            ),
        ),
        migrations.AlterField(
            model_name="log",
            name="action",
            field=models.CharField(max_length=255),
        ),
    ]