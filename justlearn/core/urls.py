from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.SimpleRouter()
router.register('Student', views.StudentProfileViewSet)
router.register('Teacher', views.TeacherProfileViewSet)

urlpatterns = [
    path('',include(router.urls))
    
]