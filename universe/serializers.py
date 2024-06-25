from rest_framework import serializers

from universe.models import Quizlet, Planet, Question, UserAnswer, Answer


class QuizletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quizlet
        fields = ('id', 'title')


class PlanetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Planet
        fields = ('id', 'name', "description", "quizlet")


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('id', "question", 'answer', "is_correct" , "planet")


class QuestionSerializer(serializers.ModelSerializer):
    # answers = AnswerSerializer(many=True)

    class Meta:
        model = Question
        fields = ('id', "question", "quizlet", "planet")


class QuestionWithAnswerSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True)

    class Meta:
        model = Question
        fields = ('id', "question", "quizlet", "answers")


class UserAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAnswer
        fields = ('id', "user", "question", "answer")
