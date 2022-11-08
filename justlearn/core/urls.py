from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('Student', views.StudentProfileViewSet)

app_name = 'core'
urlpatterns = [
    path('', include(router.urls))
]
