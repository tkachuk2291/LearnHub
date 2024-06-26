# Generated by Django 5.0.6 on 2024-06-26 10:19

import universe.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("universe", "0002_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="alphabet",
            name="image_upload",
            field=models.ImageField(
                blank=True, null=True, upload_to=universe.models.upload_to_alphabet
            ),
        ),
        migrations.AlterField(
            model_name="alphabet",
            name="audio_file",
            field=models.FileField(upload_to=universe.models.upload_audio_file),
        ),
    ]
