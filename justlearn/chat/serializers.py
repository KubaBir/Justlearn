from attr import fields
from core.models import Chat, Message
from rest_framework import serializers


class MessageSerializer(serializers.ModelSerializer):
    # receiver = serializers.CharField(write_only=True)

    class Meta:
        model = Message
        fields = ['content', 'timestamp']
        read_only_fields = ['timestamp']


class ChatSerializer(serializers.ModelSerializer):
    # participants = serializers.ListField()

    class Meta:
        model = Chat
        fields = ['id', 'participants']


class ChatDetailSerializer(serializers.ModelSerializer):
    messages = serializers.ListField(source='get_messages')
    participants = serializers.ListField(source='get_participants')

    class Meta:
        model = Chat
        fields = ['id', 'participants', 'messages']
