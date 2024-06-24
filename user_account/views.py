from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView

from user_account.models import User
from user_account.serializers import UserSerializer, TokenObtainPairSerializer


class UserWineViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    model = User
    serializer_class = UserSerializer


class RegisterView(APIView):
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            get_user_model().objects.create_user(**serializer.validated_data)
            return JsonResponse({"message": "Account created successfully"}, status=HTTP_201_CREATED)
        return JsonResponse({"errors": serializer.errors}, status=HTTP_400_BAD_REQUEST)


class EmailTokenObtainPairView(TokenObtainPairView):
    serializer_class = TokenObtainPairSerializer
