from django.shortcuts import render
from core.views import UserProfileViewSet
from core.views import TeacherPermissions
from .serializers import TeacherProfileSerializer, TeacherProfilePicSerializer
from core.models import Teacher
# Create your views here.

class TeacherProfileViewSet(UserProfileViewSet):
    permission_classes = [TeacherPermissions]
    serializer_class = TeacherProfileSerializer
    queryset = Teacher.objects.all()

    def get_serializer_class(self):
        if self.action == 'upload_image':
            return TeacherProfileSerializer
        else:
            return TeacherProfilePicSerializer
    