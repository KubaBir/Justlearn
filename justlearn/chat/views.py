from core.models import Chat, Message, User
from django.conf import settings
from django.core.mail import send_mail
from rest_framework import mixins, status, views, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.serializers import Serializer

from . import serializers


class SendMessageView(viewsets.GenericViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Chat.objects.all()
    serializer_class = serializers.MessageSerializer


class ChatViewSet(
        mixins.ListModelMixin,
        mixins.RetrieveModelMixin,
        viewsets.GenericViewSet):
    serializer_class = serializers.ChatSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Chat.objects.all()
    serializer_class = serializers.ChatSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.ChatSerializer
        if self.action == 'send_message':
            return serializers.MessageSerializer
        if self.action == 'create_chat':
            return serializers.ChatCreateSerializer
        if self.action == 'add_to_chat':
            return serializers.ChatAddUserSerializer
        if self.action == 'leave':
            return Serializer
        return serializers.ChatDetailSerializer

    @action(methods=['POST'], detail=True)
    def send_message(self, request, pk=None):
        chat = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            message = serializer.save(author=self.request.user)
            chat.messages.add(message)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['POST'], detail=False)
    def create_chat(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            chat = Chat.objects.create()
            chat.participants.add(self.request.user)
            for inv in serializer.data['invitations']:
                user = User.objects.get(name=inv)
                chat.participants.add(user)
                send_mail('You have been invited to a chat - Juslearn!', f'Hi {user.name}, {request.user.name} has started a chat with you ',settings.DEFAULT_FROM_EMAIL, user.email)
            chat.save
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['POST'], detail=True)
    def add_to_chat(self, request, pk=None):
        chat = self.get_object()
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            for user in serializer.data['users']:
                if user not in chat.get_participants():
                    user = User.objects.get(name=user)
                    chat.participants.add(user)
                    send_mail('You have been added to a chat - Juslearn!', f'Hi {user.name}, {request.user.name} has added you to a chat  ',settings.DEFAULT_FROM_EMAIL, user.email)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['POST'], detail=True)
    def leave(self, request, pk=None):
        chat = self.get_object()
        # serializer = self.get_serializer(data=request.data)
        # if serializer.is_valid():
        chat.participants.remove(self.request.user)
        return Response({"Success"}, status=status.HTTP_200_OK)
