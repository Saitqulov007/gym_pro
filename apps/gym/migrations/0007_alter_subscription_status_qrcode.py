# Generated by Django 4.2.3 on 2023-12-12 18:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("gym", "0006_gymsession_subscription"),
    ]

    operations = [
        migrations.AlterField(
            model_name="subscription",
            name="status",
            field=models.CharField(
                choices=[("active", "Активный"), ("inactive", "Неактивный")],
                default="active",
                max_length=15,
            ),
        ),
        migrations.CreateModel(
            name="QRCode",
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
                ("code", models.CharField(max_length=100, unique=True)),
                ("image", models.ImageField(upload_to="qr_codes/")),
                ("is_printed", models.BooleanField(default=False)),
                (
                    "user",
                    models.OneToOneField(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
