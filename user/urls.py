from django.urls import path, include, re_path
from .views import *
from rest_framework import routers
from dj_rest_auth.registration.views import VerifyEmailView

router = routers.DefaultRouter()
router.register('user', UserViewSet) # 유저리스트 (테스트용)

# api/user/
urlpatterns = [
    path("", include(router.urls)),
    path('kakao/login', kakao_login, name='kakao_login'),
    path('kakao/callback/', kakao_callback, name='kakao_callback'),
    path('kakao/login/finish/', KakaoLogin.as_view(), name='kakao_login_todjango'),
]