from rest_framework import serializers
from .models import ApexModel


class ApexSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApexModel
        fields = ('title', 'description', 'created_at')
