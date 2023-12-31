# Generated by Django 4.2.7 on 2023-11-08 16:03

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="api",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("api_key", models.TextField()),
                ("No_use", models.CharField(default=0, max_length=100)),
                ("created", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="asked_Ai",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("question", models.TextField(blank=True)),
                ("answer", models.TextField(blank=True)),
                ("created", models.DateTimeField(auto_now_add=True)),
                (
                    "api",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="NOverBackend.api",
                    ),
                ),
            ],
        ),
    ]
