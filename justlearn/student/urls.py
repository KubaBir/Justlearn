from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import StudentProfileViewSet

router = DefaultRouter()
router.register('', StudentProfileViewSet)

app_name = 'student'
urlpatterns = [
    path('', include(router.urls)),
]
