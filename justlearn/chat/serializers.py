from attr import fields
from core.models import Chat, Message, User
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
        read_only_fields = ['id', 'participants']


class ChatDetailSerializer(serializers.ModelSerializer):
    messages = serializers.ListField(source='get_messages')
    participants = serializers.ListField(source='get_participants')

    class Meta:
        model = Chat
        fields = ['id', 'participants', 'messages']


class ChatCreateSerializer(serializers.Serializer):
    invitations = serializers.ListField()

    def validate_invitations(self, field):
        for inv in field:
            if not User.objects.filter(name=inv).count() == 1:
                raise serializers.ValidationError(f"User {inv} not found")
        return field


class ChatAddUserSerializer(serializers.Serializer):
    users = serializers.ListField()

    def validate_users(self, field):
        for user in field:
            if not User.objects.filter(name=user).count() == 1:
                raise serializers.ValidationError(f"User {user} not found")
        return field
