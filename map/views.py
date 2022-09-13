from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class PathViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated] # Header - Bearer <access 토큰> 담아서 요청
    queryset = Path.objects.all()
    serializer_class = PathSerializer

class SpotViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Spot.objects.all()
    serializer_class = SpotSerializer

# km에 해당하는 모든 경로 반환
class CategoryPath(APIView):
    def get(self, request, km):
        path_list = Path.objects.filter(length_category=km)
        serializer_context = {'request': request,}
        serializer_class = PathSerializer(path_list, many=True, context=serializer_context)
        return Response({"km":km, "path_list":serializer_class.data})