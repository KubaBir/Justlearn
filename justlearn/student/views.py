from core.models import Student
from core.views import UserProfileViewSet

from .serializers import StudentProfileSerializer


class StudentProfileViewSet(UserProfileViewSet):
    serializer_class = StudentProfileSerializer
    queryset = Student.objects.all()
