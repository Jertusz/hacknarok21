# Generated by Django 3.1.7 on 2021-03-27 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0003_auto_20210327_1939"),
    ]

    operations = [
        migrations.AddField(
            model_name="sessionlog",
            name="admin",
            field=models.CharField(max_length=255, null=True),
        ),
    ]
