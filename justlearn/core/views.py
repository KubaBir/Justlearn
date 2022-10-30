from django.shortcuts import render

from .serializers import StudentProfileSerializer
from . models import User, Student, Teacher
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.response import Response
# Create your views here.

class StudentProfileViewSet(viewsets.ModelViewSet):
    serializer_class = StudentProfileSerializer
    queryset = Student.objects.all()
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    @action(methods=["GET", "PATCH"], detail=False)
    def my_profile(self,request):
        obj = Student.objects.filter(user= self.request.user).get()
        serializer = self.get_serializer(obj)
        return Response(serializer.data)


    



