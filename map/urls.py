from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('path', PathViewSet) # 경로 -> 127.0.0.1:8000/api/map/path
router.register('spot', SpotViewSet) # 스팟 -> 127.0.0.1:8000/api/map/spot

# api/map/
urlpatterns = [
    path("", include(router.urls)),
    path("categorypath/<int:km>", CategoryPath.as_view())
    # path('kakao/login', kakao_login, name='kakao_login'),
]