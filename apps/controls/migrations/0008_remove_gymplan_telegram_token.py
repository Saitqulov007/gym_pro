# Generated by Django 4.2.3 on 2024-03-05 09:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("controls", "0007_gymplan_telegram_token"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="gymplan",
            name="telegram_token",
        ),
    ]
