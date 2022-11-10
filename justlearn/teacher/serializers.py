from rest_framework import serializers
from core.serializers import SkillSerializer, AdvertisementSerializer
from core.models import Teacher

class TeacherProfileSerializer(serializers.ModelSerializer):
    skills = SkillSerializer(many=True)
    advertisement_set = AdvertisementSerializer(many=True, read_only=True)

    class Meta:
        model = Teacher
        fields = ['user', 'skills', 'github_link', 'linkedin_link',
                  'description', 'rating', 'advertisement_set']
        read_only_fields = ['rating']

class TeacherProfilePicSerializer(serializers.ModelSerializer):

    class Meta:
        model = Teacher
        fields = ['id', 'image']
        read_only_fields = ['id']
        extra_kwargs = {'image': {'required': 'True'}}
