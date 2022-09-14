from .models import *
from rest_framework import serializers

class ActivitySerializer(serializers.ModelSerializer):
    path_name = serializers.ReadOnlyField(source='path_id.name')
    class Meta:
        model = Activity
        fields = '__all__'