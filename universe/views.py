from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from universe.models import Quizlet, Planet, Question, UserAnswer, Answer, Alphabet
from universe.serializers import QuizletSerializer, QuestionSerializer, UserAnswerSerializer, PlanetSerializer, \
    AnswerSerializer, QuestionWithAnswerSerializer, ImageSerializer, AudioFileSerializer, AlphabetSerializer


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

    def get_serializer_class(self):
        if self.action == "list":
            return QuestionSerializer
        elif self.action == "upload_image":
            return ImageSerializer
        elif self.action == "create":
            return QuestionSerializer
        return QuestionSerializer

    @action(methods=["POST"], detail=True, url_path="upload-image")
    def upload_image(self, request):
        learn_hub = self.get_object()
        serializer = self.get_serializer(learn_hub, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class AnswerViewSet(viewsets.ModelViewSet):
    model = Answer
    serializer_class = AnswerSerializer
    queryset = Answer.objects.all()
    # lookup_field = 'id'

    def get_serializer_class(self):
        if self.action == "list":
            return AnswerSerializer
        elif self.action == "upload-audio-file":
            return AudioFileSerializer
        elif self.action == "create":
            return AnswerSerializer
        return AnswerSerializer

    @action(methods=["POST"], detail=True, url_path="upload-audio-file")
    def upload_audio_file(self, request):
        learn_hub = self.get_object()
        serializer = self.get_serializer(learn_hub, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)



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


class AlphabetViewSet(viewsets.ModelViewSet):
    model = Alphabet
    serializer_class = AlphabetSerializer
    queryset = Alphabet.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return AlphabetSerializer
        elif self.action == "upload-audio-file":
            return AudioFileSerializer
        elif self.action == "upload_image":
            return ImageSerializer
        elif self.action == "create":
            return AlphabetSerializer
        return AlphabetSerializer

    @action(methods=["POST"], detail=True, url_path="upload-audio-file")
    def upload_audio_file(self, request):
        learn_hub = self.get_object()
        serializer = self.get_serializer(learn_hub, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(methods=["POST"], detail=True, url_path="upload-image")
    def upload_image(self, request):
        learn_hub = self.get_object()
        serializer = self.get_serializer(learn_hub, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)