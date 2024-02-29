from rest_framework import routers
from django.urls import path, include
from .views import ProductViewSet, LessonViewSet

router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'lessons', LessonViewSet)

urlpatterns = [
    path('', include(router.urls)),
]