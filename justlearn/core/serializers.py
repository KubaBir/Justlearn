from rest_framework import serializers

from .models import (Advertisement, Exercise, Lesson, Problem, Skill, Student,
                     Teacher)


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'


class AdvertisementSerializer(serializers.ModelSerializer):
    #jak tutaj dodac zeby link sie tworzyl odrazu api/teachers{id}


    class Meta:
        model = Advertisement
        fields = ['id','title','teacher','link','description']
        read_only_fields = ('id', 'teacher','link')

    def create(self, validated_data):
        link = f"api/teachers/{super.request.user.id}"
        advertisement  = Advertisement.model.objects.create(link, **validated_data)
        return advertisement


class ProblemSerializer(serializers.ModelSerializer):
    #jak tutaj dodac zeby link sie tworzyl odrazu api/students{id}

    class Meta:
        model = Problem
        fields = ['id', 'title','student','link' 'description']
        read_only_fields = ('id', 'student','link')

    def create(self, validated_data):
        link = f"api/students/{super.request.user.id}"
        problem  =Problem.model.objects.create(link, **validated_data)
        return Problem



class TeacherProfilePicSerializer(serializers.ModelSerializer):

    class Meta:
        model = Teacher
        fields = ['id', 'image']
        read_only_fields = ['id']
        extra_kwargs = {'image': {'required': 'True'}}


class ExerciseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Exercise
        fields = ['id', 'lesson', 'file', 'timestamp']
        read_only_fields = ('id', 'timestamp')


class LessonSerializer(serializers.ModelSerializer):
    exercise_set = ExerciseSerializer(many=True, read_only=True)

    class Meta:
        model = Lesson
        fields = ['id', 'student', 'teacher', 'duration', 'lesson_date',
                  'meeting_link', 'topic', 'description', 'exercise_set']
