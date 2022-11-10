from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import  TeacherProfileViewSet

router = DefaultRouter()
router.register('', TeacherProfileViewSet)

app_name = 'teacher'
urlpatterns = [
    path('', include(router.urls)),
]
