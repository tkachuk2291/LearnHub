from django.db import models
from user_account.models import User


class Quizlet(models.Model):
    title = models.CharField(max_length=256)

    def __str__(self):
        return self.title


class Planet(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    quizlet = models.ForeignKey(Quizlet, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Question(models.Model):
    planet = models.ForeignKey(Planet, on_delete=models.CASCADE)
    quizlet = models.ForeignKey(Quizlet, on_delete=models.CASCADE, related_name='questions')
    question = models.CharField(max_length=1024)

    def __str__(self):
        return self.question


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    answer = models.CharField(max_length=300)
    is_correct = models.BooleanField(default=False)
    planet = models.ForeignKey(Planet, on_delete=models.CASCADE)

    def __str__(self):
        return self.answer


class UserAnswer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.answer)
