from .models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'is_superuser', 'is_active', 'is_staff', 'region', 'point', 'guild']
