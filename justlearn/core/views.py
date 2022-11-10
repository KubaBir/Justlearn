from lib2to3.pytree import Base
from tokenize import Token

from core.serializers import LessonSerializer
from django.shortcuts import render
from rest_framework import mixins, status, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.generics import mixins
from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS
from rest_framework.response import Response

from .models import Lesson, Student, Teacher, User

# Create your views here.

class LessonPermissions(BasePermission):
    #czemu to nie dziala??
    def has_object_permission(self, request, view, obj):
        if request.user.is_teacher:
            if request.method in ['GET','POST','PATCH','DELETE']:
                return obj.teacher.user ==request.user
            return False
        if request.user.is_student:
            if request.method in SAFE_METHODS:
                return obj.student.user == request.user
            return False
        


class TeacherPermissions(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_teacher:
            return True


class StudentPermissions(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_student:
            return True


class UserProfileViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]

    @action(methods=["GET", "PATCH"], detail=False)
    def my_profile(self, request):
        obj = Student.objects.filter(user=self.request.user).get()
        serializer = self.get_serializer(obj)
        return Response(serializer.data)

    @action(methods=["POST"], detail=True, url_path='upload_image')
    def upload_image(self, request, pk=None):
        """Upload an image to User's Profile."""
        user = self.get_object()
        serializer = self.get_serializer(user, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LessonViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [LessonPermissions]
    querysert = Lesson.objects.all()
    serializer_class = LessonSerializer

    def get_queryset(self):
        if self.request.user.is_teacher:
            qs = Lesson.objects.filter(teacher = Teacher(user = self.request.user)).all()
        else:
            qs = Lesson.objects.filter(student = Student(user = self.request.user)).all()
        return qs
    




