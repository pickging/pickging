from .models import *
from rest_framework import serializers

class PathSerializer(serializers.ModelSerializer):
    class Meta:
        model = Path
        fields = '__all__'

class SpotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Spot
        fields = '__all__'
