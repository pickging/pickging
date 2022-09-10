from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from .models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticated

from user.models import User
from user.serializers import UserSerializer

"""
길드 CRUD
path: /api/guild/guild/

"""
class GuildViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = GuildSerializer
    queryset = Guild.objects.all()


"""
길드 가입(GET), 탈퇴(DELETE)
path: /api/guild/inout/:guild_id/

"""
class InOutGuild(APIView):
    def get(self, request, guild_id):
        permission_classes = [IsAuthenticated]
        guild_list = Guild.objects.all().order_by('-member_number')
        guild = Guild.objects.filter(pk=guild_id).first()
        if guild:
            user = User.objects.filter(email=request.user).first()
            user.guild = guild
            user.save()
            guild.member_number = guild.member_number + 1
            guild.save()
            serializer_context = {'request': request,}
            serializer_class = GuildSerializer(guild_list, many=True, context=serializer_context)
            user_serializer = UserSerializer(user)
            return Response({"user": user_serializer.data, "guild_list": serializer_class.data})
        else:
            raise Http404("길드 존재하지 않음~!~")
        
    def delete(self, request, guild_id):
        permission_classes = [IsAuthenticated]
        guild_list = Guild.objects.all().order_by('-member_number')
        guild = Guild.objects.filter(pk=guild_id).first()
        
        if guild:
            user = User.objects.filter(email=request.user).first()
            user.guild = None
            user.save()
            guild.member_number = guild.member_number - 1
            if guild.member_number:
                guild.save()
            else:
                guild.delete()
            serializer_context = {'request': request,}
            serializer_class = GuildSerializer(guild_list, many=True, context=serializer_context)
            user_serializer = UserSerializer(user)
            return Response({"user": user_serializer.data, "guild_list": serializer_class.data})
        else:
            raise Http404("길드 존재하지 않음~!~")
    
    # def delete(self, request, id):