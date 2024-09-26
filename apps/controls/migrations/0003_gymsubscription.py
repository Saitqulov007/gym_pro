# Generated by Django 4.2.3 on 2024-02-01 12:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("controls", "0002_rename_sessions_gymplan_members_limit"),
    ]

    operations = [
        migrations.CreateModel(
            name="GymSubscription",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "status",
                    models.CharField(
                        choices=[("active", "Активный"), ("inactive", "Неактивный")],
                        default="active",
                        max_length=15,
                    ),
                ),
                ("start_date", models.DateField()),
                ("end_date", models.DateField()),
                (
                    "gym",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="controls.gym"
                    ),
                ),
                (
                    "plan",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="controls.gymplan",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
