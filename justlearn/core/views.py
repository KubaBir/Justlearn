from datetime import date as dt
from lib2to3.pytree import Base
from tokenize import Token

from core.serializers import (AdvertisementSerializer, LessonSerializer,
                              ProblemSerializer)
from django.shortcuts import render
from rest_framework import mixins, status, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.generics import mixins
from rest_framework.permissions import (SAFE_METHODS, BasePermission,
                                        IsAuthenticated)
from rest_framework.response import Response

from .models import Advertisement, Lesson, Problem, Student, Teacher, User


class LessonPermissions(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return obj.student == Student.objects.get(user=request.user)
        return obj.teacher == Teacher.objects.get(user=request.user)

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        else:
            return request.user.is_teacher


class ProblemPermissions(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        else:
            return obj.student == Student.objects.get(user=request.user)

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        else:
            return request.user.is_student


class AdvertisementPermissions(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        else:
            return obj.teacher == Teacher.objects.get(user=request.user)

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        else:
            return request.user.is_teacher


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
            qs = Lesson.objects.filter(teacher=Teacher.objects.get(
                user=self.request.user)).filter(lesson_date__gt=dt.today()).all()
            # czemu nie czyta lesson_date
        if self.request.user.is_student:
            qs = Lesson.objects.filter(student=Student.objects.get(
                user=self.request.user)).filter(lesson_date__gt=dt.today()).all()
        return qs
    # @action(methods = ["GET"], detail = False)
    # tu trzeba dokonczyc
    # def previous_lessons(self,request):
        # tu trzeba odwolac do qs i filter lesson_date < dt.today() + ustawic zeby celery usuwalo lekcje starsze niz np tydzien.


class ProblemViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [ProblemPermissions]
    queryset = Problem.objects.all()
    serializer_class = ProblemSerializer

    def perform_create(self, serializer):
        serializer.save(student=Student.objects.get(user=self.request.user))


class AdvertisementViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [AdvertisementPermissions]
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer

    def perform_create(self, serializer):
        serializer.save(teacher=Teacher.objects.get(user=self.request.user))
