from core.models import Teacher
from core.views import TeacherPermissions, UserProfileViewSet
from django.shortcuts import render

from .serializers import TeacherProfilePicSerializer, TeacherProfileSerializer

# Create your views here.


class TeacherProfileViewSet(UserProfileViewSet):
    permission_classes = [TeacherPermissions]
    serializer_class = [TeacherProfileSerializer]
    queryset = Teacher.objects.all()

    def get_serializer_class(self):
        if self.action == 'upload_image':
            return TeacherProfilePicSerializer
        else:
            return TeacherProfileSerializer
