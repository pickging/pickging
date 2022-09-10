from django.urls import path, include, re_path
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('guild', GuildViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('inout/<int:guild_id>', InOutGuild.as_view()),
]