from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import ChatViewSet, SendMessageView

router = DefaultRouter()
router.register('', SendMessageView)
router.register('', ChatViewSet)

app_name = 'chat'
urlpatterns = [
    path('', include(router.urls)),
]
