from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('user', UserViewSet) # 유저리스트 (테스트용)

# api/user/
urlpatterns = [
    path("", include(router.urls)),
    path('kakao/login', kakao_login, name='kakao_login'),
    # 카카오 소셜로그인 -> 127.0.0.1:8000/api/user/kakao/login 으로 접속시 카카오창으로 자동 리다이렉트
    path('kakao/callback/', kakao_callback, name='kakao_callback'),
    path('kakao/login/finish/', KakaoLogin.as_view(), name='kakao_login_todjango'),

    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    # 토큰 재발급 -> 127.0.0.1:8000/api/user/dj-rest-auth/token/refresh/ 으로 {refresh:"토큰"} 전송

    path('edit/', UserEdit.as_view()),
    path('current/', CurrentUser.as_view()),
    path('<int:user_id>/activity', UserActivity.as_view()),
]