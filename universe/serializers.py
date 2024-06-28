from rest_framework import serializers

from universe.models import Quizlet, Planet, Question, UserAnswer, Answer, Alphabet


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
        fields = ('id', "question", 'answer', "is_correct", "planet", "audio_file")

    def perform_create(self, serializer):
        serializer.save()


class QuestionSerializer(serializers.ModelSerializer):
    # answers = AnswerSerializer(many=True)

    class Meta:
        model = Question
        fields = ('id', "question", "quizlet", "planet", "image_upload")


class QuestionWithAnswerSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True)

    class Meta:
        model = Question
        fields = ('id', "question", "quizlet", "answers")


class UserAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAnswer
        fields = ('id', "user", "question", "answer")


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ("id", "image_upload",)


class AudioFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ("id", "audio_file",)


class AlphabetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alphabet
        fields = ("id", "char", "audio_file", "image_upload")
