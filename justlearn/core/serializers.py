from rest_framework import serializers

from .models import Advertisement, Problem, Skill, Student, Teacher


class SkillSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Skill
        fields = '__all__'
class AdvertisementSerializer(serializers.ModelSerializer):

    class Meta:
        model = Advertisement
        fields = '__all__'
class ProblemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Problem
        fields = '__all__'

class TeacherProfileSerializer(serializers.ModelSerializer):
    skills = SkillSerializer(many = True)
    advertisement_set = AdvertisementSerializer(many = True, read_only = True)
    class Meta:
        model = Teacher
        fields = ['user', 'skills', 'github_link', 'linkedin_link', 'description','rating','advertisement_set']
        read_only_fields = ['rating']

class StudentProfileSerializer(serializers.ModelSerializer):
    skills = SkillSerializer(many = True)
    problem_set = ProblemSerializer(many = True, read_only = True)
    class Meta:
        model  = Student
        fields = ['user','skills','github_link','linkedin_link','description','problem_set']

class ProfilePicSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ['id','image']
        read_only_fields = ['id']
        extra_kwargs = {'image':{'required':'True' }} 
        
