from .models import *
from rest_framework import serializers

class ActivitySerializer(serializers.ModelSerializer):
    nickname = serializers.ReadOnlyField(source='user_id.nickname')
    path_name = serializers.ReadOnlyField(source='path_id.name')
    class Meta:
        model = Activity
        fields = '__all__'