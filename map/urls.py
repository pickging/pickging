from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('path', PathViewSet) # 경로
router.register('spot', SpotViewSet) # 스팟

# api/map/
urlpatterns = [
    path("", include(router.urls)),
    # path('kakao/login', kakao_login, name='kakao_login'),
]