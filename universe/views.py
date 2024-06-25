from django.shortcuts import render
from rest_framework import viewsets

from universe.models import Quizlet, Planet, Question, UserAnswer, Answer
from universe.serializers import QuizletSerializer, QuestionSerializer, UserAnswerSerializer, PlanetSerializer, \
    AnswerSerializer, QuestionWithAnswerSerializer


class QuizletViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAdminOrReadOnly]
    model = Quizlet
    serializer_class = QuizletSerializer
    queryset = Quizlet.objects.all()


class PlanetViewSet(viewsets.ModelViewSet):
    model = Planet
    serializer_class = PlanetSerializer
    queryset = Planet.objects.all()


class QuestionViewSet(viewsets.ModelViewSet):
    model = Question
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()


class AnswerViewSet(viewsets.ModelViewSet):
    model = Answer
    serializer_class = AnswerSerializer
    queryset = Answer.objects.all()
    lookup_field = 'id'


class QuestionWithAnswerViewSet(viewsets.ModelViewSet):
    model = Question
    serializer_class = QuestionWithAnswerSerializer
    queryset = Question.objects.all()

    # def get_queryset(self):
    #     question_id = self.request.query_params.get('question_id')
    #     if question_id is not None:
    #         return Answer.objects.filter(question_id=question_id)
    #     return Answer.objects.all()


class UserAnswerViewSet(viewsets.ModelViewSet):
    model = UserAnswer
    serializer_class = UserAnswerSerializer
    queryset = UserAnswer.objects.all()
