# Generated by Django 4.1.7 on 2023-03-12 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="is_manager",
            field=models.BooleanField(default=False),
        ),
    ]
