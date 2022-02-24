# Generated by Django 3.2.11 on 2022-02-24 09:19

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("authnapp", "0004_alter_shopuser_age"),
    ]

    operations = [
        migrations.CreateModel(
            name="ShopUserProfile",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("tagline", models.CharField(blank=True, max_length=128, verbose_name="теги")),
                ("aboutMe", models.TextField(blank=True, max_length=512, verbose_name="о себе")),
                (
                    "gender",
                    models.CharField(
                        blank=True, choices=[("M", "Мужской"), ("W", "Женский")], max_length=1, verbose_name="пол"
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
                ),
            ],
        ),
    ]
