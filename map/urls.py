from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('path', PathViewSet) # 경로 -> 127.0.0.1:8000/api/map/path/<km수> -> 1,3,5km 경로 반환
router.register('spot', SpotViewSet) # 스팟 -> 127.0.0.1:8000/api/map/spot -> 모든 스팟 반환

# api/map/
urlpatterns = [
    path("", include(router.urls)),
    # path('kakao/login', kakao_login, name='kakao_login'),
]