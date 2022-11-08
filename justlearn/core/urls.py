from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('Teacher', views.TeacherProfileViewSet)

app_name = 'core'
urlpatterns = [
    path('', include(router.urls))
]
