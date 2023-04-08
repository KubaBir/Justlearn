from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
#router.register('lessons',views.LessonViewSet, basename = 'lessons')
router.register('problems', views.ProblemViewSet)
router.register('advertisements', views.AdvertisementViewSet)
app_name = 'main_page'
urlpatterns = [
    path('', include(router.urls))
]
