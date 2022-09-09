from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *

# Create your views here.
class GuildViewSet(ModelViewSet):
    serializer_class = GuildSerializer
    queryset = Guild.objects.all()