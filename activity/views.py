from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from user.models import *

# Create your views here.
class ActivityViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

    def perform_create(self, serializer):
        a = serializer.save(user_id=self.request.user)
        user = User.objects.get(email=self.request.user)
        user.point += a.point
        user.save()
        # print("잔여포인트: ", user.point)