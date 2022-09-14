from .serializers import *
from .models import *
from activity.serializers import *
from activity.models import *
import requests, os
from json import JSONDecodeError
from django.http import JsonResponse
from django.shortcuts import redirect
from rest_framework import status, viewsets
from rest_framework.views import APIView
from allauth.socialaccount.models import SocialAccount
from dj_rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from allauth.socialaccount.providers.kakao import views as kakao_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserEdit(APIView):
    def post(self, request):
        nickname = request.data.get("nickname")
        region = request.data.get("region")
        # print(request.user, region)
        user = User.objects.get(email=request.user)
        user.nickname = nickname
        user.region = region
        user.save()
        user_serializer = UserSerializer(user)
        return Response({"user":user_serializer.data})

class CurrentUser(APIView):
    def get(self, request):
        permission_classes = [IsAuthenticated]
        user = User.objects.get(email=request.user)
        user_serializer = UserSerializer(user)
        return Response({"user":user_serializer.data})

class UserActivity(APIView):
    def get(self, request, user_id):
        permission_classes = [IsAuthenticated]
        user = User.objects.get(email=request.user)
        
        if user_id != user.id:
            return JsonResponse({'err_msg': '토큰 유저와 user_id 유저가 일치하지 않음'}, status=status.HTTP_401_UNAUTHORIZED)

        user_serializer = UserSerializer(user)
        activity_list = Activity.objects.filter(user_id=user_id)
        activity_serializer = ActivitySerializer(activity_list)
        print("activity_list ===>", activity_serializer)
        return Response({"user":user_serializer.data, "activity":activity_serializer.data})


BASE_URL = 'http://127.0.0.1:8000/'
KAKAO_CALLBACK_URI = BASE_URL + 'api/user/kakao/callback/'

# 카카오 로그인 창
def kakao_login(request):
    client_id = os.environ.get("SOCIAL_AUTH_KAKAO_CLIENT_ID")
    return redirect(f"https://kauth.kakao.com/oauth/authorize?client_id={client_id}&redirect_uri={KAKAO_CALLBACK_URI}&response_type=code&scope=account_email") # 이메일 수집 동의

def kakao_callback(request):
    client_id = os.environ.get("SOCIAL_AUTH_KAKAO_CLIENT_ID")
    code = request.GET.get("code")
    # code로 access token 요청
    token_request = requests.get(f"https://kauth.kakao.com/oauth/token?grant_type=authorization_code&client_id={client_id}&redirect_uri={KAKAO_CALLBACK_URI}&code={code}")
    token_response_json = token_request.json()
    
    error = token_response_json.get("error", None)
    if error is not None:
        raise JSONDecodeError(error)

    access_token = token_response_json.get("access_token")
    # access token으로 카카오톡 프로필 요청
    profile_request = requests.post(
        "https://kapi.kakao.com/v2/user/me",
        headers={"Authorization": f"Bearer {access_token}"},
    )
    
    profile_json = profile_request.json()

    kakao_account = profile_json.get("kakao_account")
    email = kakao_account.get("email", None) # 이메일!

    # 이메일 없으면 오류 => 카카오톡 최신 버전에서는 이메일 없이 가입 가능해서 추후 수정해야함
    if email is None:
        return JsonResponse({'err_msg': 'failed to get email'}, status=status.HTTP_400_BAD_REQUEST)

    # 받아온 카카오 계정으로 회원가입/로그인 시도
    try:
        user = User.objects.get(email=email)
        social_user = SocialAccount.objects.get(user=user)

        if social_user.provider != 'kakao':
            return JsonResponse({'err_msg': 'no matching social type'}, status=status.HTTP_400_BAD_REQUEST)

        data = {'access_token': access_token, 'code': code}
        accept = requests.post(f"{BASE_URL}api/user/kakao/login/finish/", data=data)
        accept_status = accept.status_code

        if accept_status != 200:
            return JsonResponse({'err_msg': 'failed to signin'}, status=accept_status)

        accept_json = accept.json()
        accept_json.pop('user', None)
        return JsonResponse(accept_json)

    except User.DoesNotExist:
        data = {'access_token': access_token, 'code': code}
        accept = requests.post(f"{BASE_URL}api/user/kakao/login/finish/", data=data)
        accept_status = accept.status_code

        if accept_status != 200:
            return JsonResponse({'err_msg': 'failed to signup'}, status=accept_status)

        accept_json = accept.json()
        accept_json.pop('user', None)
        return JsonResponse(accept_json)

    except SocialAccount.DoesNotExist:
        return JsonResponse({'err_msg': 'email exists but not social user'}, status=status.HTTP_400_BAD_REQUEST)


class KakaoLogin(SocialLoginView):
    adapter_class = kakao_view.KakaoOAuth2Adapter
    callback_url = KAKAO_CALLBACK_URI
    client_class = OAuth2Client
