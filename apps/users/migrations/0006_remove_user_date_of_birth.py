# Generated by Django 4.2.3 on 2023-12-12 07:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0005_alter_userprofile_gender_alter_userprofile_user"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="date_of_birth",
        ),
    ]
