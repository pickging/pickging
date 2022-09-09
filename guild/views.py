from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from .models import *
from .serializers import *


# Create your views here.
"""
길드 CRUD
path: /api/guild/guild/

"""
class GuildViewSet(ModelViewSet):
    serializer_class = GuildSerializer
    queryset = Guild.objects.all()


"""
길드 가입(GET), 탈퇴(DELETE)
path: /api/guild/inout/:guild_id/

"""
class InOutGuild(APIView):
    def get(self, request, guild_id):
        guild_list = Guild.objects.all().order_by('-member_number')
        guild = Guild.objects.filter(pk=guild_id).first()
        #! 유저 guild 수정하기
        
        if guild:
            guild.member_number = guild.member_number + 1
            guild.save()
            serializer_context = {'request': request,}
            serializer_class = GuildSerializer(guild_list, many=True, context=serializer_context)
            #! 유저 serialize 같이 보내주기
            return Response({"guild_list": serializer_class.data})
        else:
            raise Http404("길드 존재하지 않음~!~")
        
    def delete(self, request, guild_id):
        guild_list = Guild.objects.all().order_by('-member_number')
        guild = Guild.objects.filter(pk=guild_id).first()
        #! 유저 guild 수정하기
        
        if guild:
            guild.member_number = guild.member_number - 1
            guild.save()
            serializer_context = {'request': request,}
            serializer_class = GuildSerializer(guild_list, many=True, context=serializer_context)
            #! 유저 serialize 같이 보내주기
            return Response({"guild_list": serializer_class.data})
        else:
            raise Http404("길드 존재하지 않음~!~")
    
    # def delete(self, request, id):