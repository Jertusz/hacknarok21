# Generated by Django 3.1.7 on 2021-03-27 19:46

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0005_auto_20210327_1946"),
    ]

    operations = [
        migrations.AlterField(
            model_name="sessionlog",
            name="users",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.CharField(max_length=255), default=list, size=None
            ),
        ),
    ]
