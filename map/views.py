from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class PathViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated] # Header - Bearer <access 토큰> 담아서 요청
    queryset = Path.objects.all()
    serializer_class = PathSerializer

class SpotViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Spot.objects.all()
    serializer_class = SpotSerializer