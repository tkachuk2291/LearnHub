# Generated by Django 5.0.6 on 2024-06-30 15:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("universe", "0004_alter_alphabet_audio_file"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="planet",
            name="alphabet",
        ),
    ]
