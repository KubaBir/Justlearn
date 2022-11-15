from core.models import Student
from core.views import StudentPermissions, UserProfileViewSet

from .serializers import StudentProfilePicSerializer, StudentProfileSerializer


class StudentProfileViewSet(UserProfileViewSet):
    permission_classes = [StudentPermissions]
    serializer_class = StudentProfileSerializer
    queryset = Student.objects.all()

    def get_serializer_class(self):
        if self.action == 'upload_image':
            return StudentProfilePicSerializer
        else:
            return StudentProfileSerializer