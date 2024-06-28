from django.db import models
from user_account.models import User
from pathlib import Path


class Quizlet(models.Model):
    title = models.CharField(max_length=256)

    def __str__(self):
        return self.title


def upload_alphabet_audio_file(instance, filename):
    path = Path(f"upload/alphabet/{filename}")
    return path


def upload_to_alphabet(instance, filename):
    alphabet = instance.char

    path = Path(f"upload/alphabet-img/{filename}")
    return path


class Alphabet(models.Model):
    char = models.CharField(max_length=2, unique=True, null=True, blank=True)
    audio_file = models.FileField(upload_to=upload_alphabet_audio_file, null=False, blank=False)
    image_upload = models.ImageField(upload_to=upload_to_alphabet, null=True, blank=True)

    def __str__(self):
        return self.char


class Planet(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    quizlet = models.ForeignKey(Quizlet, on_delete=models.CASCADE)
    alphabet = models.ForeignKey(Alphabet, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


def upload_to(instance, filename):
    question = instance.question

    path = Path(f"upload/question/{question}")
    return path


def upload_audio_file(instance, filename):
    path = Path(f"upload/music/{filename}")
    return path


class Question(models.Model):
    planet = models.ForeignKey(Planet, on_delete=models.CASCADE)
    quizlet = models.ForeignKey(Quizlet, on_delete=models.CASCADE, related_name='questions')
    question = models.CharField(max_length=1024)
    image_upload = models.ImageField(upload_to=upload_to, null=True, blank=True)

    def __str__(self):
        return self.question

    def save(self, *args, **kwargs):
        if not self.image_upload:
            self.image_upload = None
        super().save(*args, **kwargs)


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    answer = models.CharField(max_length=300)
    is_correct = models.BooleanField(default=False)
    planet = models.ForeignKey(Planet, on_delete=models.CASCADE)
    audio_file = models.FileField(upload_to=upload_audio_file, null=False, blank=False)

    def __str__(self):
        return self.answer


class UserAnswer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.answer)
