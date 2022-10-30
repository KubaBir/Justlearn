from django.contrib.auth import authenticate, get_user_model
from django.utils.translation import gettext as _
from rest_framework import serializers
from core.models import Student, Teacher



class UserSerializer(serializers.ModelSerializer):
    """Serializer for the user object"""
    class Meta:
        model = get_user_model()
        fields = ['id','email', 'password', 'name','is_student','is_teacher']
        extra_kwargs = {
            'password': {'write_only': True, 'min_length': 5},
        }

    def create(self, validated_data):
        """Create and return a user with encrypted password"""
        is_student = validated_data['is_student']
        is_teacher = validated_data['is_teacher']
        user = get_user_model().objects.create_user(**validated_data)
        if is_student:
            Student.objects.create(user=user)
        if is_teacher:
            Teacher.objects.create(user=user)

        return get_user_model().objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        """Update and return user."""
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()

        return user


class AuthTokenSerializer(serializers.Serializer):
    """Serializer for the user authh token."""
    email = serializers.EmailField()
    password = serializers.CharField(style={"input_type": 'password'},
                                     trim_whitespace=False,)

    def validate(self, attrs):
        """Validate and auth the user."""
        email = attrs.get('email')
        password = attrs.get('password')
        user = authenticate(
            request=self.context.get('request'),
            username=email,
            password=password,
        )
        
        if not user:
            msg = _('Unable to authenticate with provided credentials')
            raise serializers.ValidationError(msg, code='authorization')
        attrs['user'] = user
        return attrs