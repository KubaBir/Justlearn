from lib2to3.pytree import Base
from tokenize import Token

from django.shortcuts import render
from rest_framework import mixins, status, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.generics import mixins
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework.response import Response

from core.serializers import ProfilePicSerializer

from .models import Student, Teacher, User
from .serializers import StudentProfileSerializer, TeacherProfileSerializer, ProfilePicSerializer

# Create your views here.

class TeacherPermissions(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_teacher:
            return True
class StudentPermissions(BasePermission):
    def has_permission(self, request, view):
        if  request.user.is_student:
            return True

class UserProfileViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]

    @action(methods=["GET", "PATCH"], detail=False)
    def my_profile(self,request):
        obj = Student.objects.filter(user= self.request.user).get()
        serializer = self.get_serializer(obj)
        return Response(serializer.data)
    @action(methods= ["POST"], detail = True, url_path = 'upload_image', serializer_class = ProfilePicSerializer)
    def upload_image(self, request, pk=None):
        """Upload an image to User's Profile."""
        user = self.get_object()
        serializer = self.get_serializer(user, data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)
        
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class StudentProfileViewSet(UserProfileViewSet):
    permission_classes = [StudentPermissions]
    serializer_class = StudentProfileSerializer
    queryset = Student.objects.all()


class TeacherProfileViewSet(UserProfileViewSet):
    permission_classes = [TeacherPermissions]
    serializer_class = TeacherProfileSerializer
    queryset = Teacher.objects.all()
    




    



