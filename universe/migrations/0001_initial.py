# Generated by Django 5.0.6 on 2024-06-26 10:16

import django.db.models.deletion
import universe.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Alphabet",
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
                (
                    "char",
                    models.CharField(blank=True, max_length=2, null=True, unique=True),
                ),
                (
                    "audio_file",
                    models.FileField(upload_to=universe.models.upload_audio_file),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Quizlet",
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
                ("title", models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name="Planet",
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
                ("name", models.CharField(max_length=256)),
                ("description", models.TextField()),
                (
                    "alphabet",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="universe.alphabet",
                    ),
                ),
                (
                    "quizlet",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="universe.quizlet",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Question",
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
                ("question", models.CharField(max_length=1024)),
                (
                    "image_upload",
                    models.ImageField(
                        blank=True, null=True, upload_to=universe.models.upload_to
                    ),
                ),
                (
                    "planet",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="universe.planet",
                    ),
                ),
                (
                    "quizlet",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="questions",
                        to="universe.quizlet",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Answer",
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
                ("answer", models.CharField(max_length=300)),
                ("is_correct", models.BooleanField(default=False)),
                (
                    "audio_file",
                    models.FileField(upload_to=universe.models.upload_audio_file),
                ),
                (
                    "planet",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="universe.planet",
                    ),
                ),
                (
                    "question",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="answers",
                        to="universe.question",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="UserAnswer",
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
                (
                    "answer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="universe.answer",
                    ),
                ),
                (
                    "question",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="universe.question",
                    ),
                ),
            ],
        ),
    ]