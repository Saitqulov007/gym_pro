# Generated by Django 4.2.3 on 2024-02-26 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0011_alter_user_roles"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="telegram_id",
            field=models.CharField(blank=True, max_length=30, null=True, unique=True),
        ),
    ]
