# Generated by Django 4.2.3 on 2024-01-23 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("gym", "0011_remove_subscription_gym"),
    ]

    operations = [
        migrations.AddIndex(
            model_name="subscription",
            index=models.Index(
                fields=["member"], name="gym_subscri_member__f91a02_idx"
            ),
        ),
    ]
