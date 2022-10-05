import email
from django.contrib.auth import get_user_model
from django.urls import path , include
from django.contrib import admin
from rest_framework import status , routers
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from rest_framework.generics import ListAPIView,ListCreateAPIView,CreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import UserSerializer

User = get_user_model()

class AdminUserListCreate(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class RegisterNewUser(CreateAPIView):
    authentication_classes = []
    permission_classes = []
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def perform_create(self, serializer):
        instance = serializer.save()
        instance.set_password(instance.password)
        instance.save()

class UserList(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    def get_queryset(self):
        """
        This view should return a list of all the information
        for the currently authenticated user.
        """
        user = self.request.user
        return User.objects.filter(email=user)

class UserRetrieveDestroyUpdate(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

'''class UserViewSet(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get_queryset(self, *args, **kwargs):
        assert isinstance(self.request.user.id, int)
        return self.queryset.filter(id=self.request.user.id)

    @action(detail=False)
    def me(self, request):
        serializer = UserSerializer(request.user, context={"request": request})
        return Response(status=status.HTTP_200_OK, data=serializer.data)
'''