from core.models import Chat, Message
from rest_framework import mixins, status, views, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response

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
    permission_classes = [IsAuthenticated]
    queryset = Chat.objects.all()
    serializer_class = serializers.ChatSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.ChatSerializer
        if self.action == 'send_message':
            return serializers.MessageSerializer
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
