from core.models import Student
from core.serializers import ProblemSerializer, SkillSerializer
from rest_framework import serializers


class StudentProfileSerializer(serializers.ModelSerializer):
    skills = SkillSerializer(many=True)
    problem_set = ProblemSerializer(many=True, read_only=True)

    class Meta:
        model = Student
        fields = ['user', 'skills', 'github_link',
                  'linkedin_link', 'description', 'problem_set','image']

class StudentProfilePicSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ['id', 'image']
        read_only_fields = ['id']
        extra_kwargs = {'image': {'required': 'True'}}
