from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('lessons',views.LessonViewSet, basename = 'lessons')
app_name = 'core'
urlpatterns = [
    path('', include(router.urls))
]
