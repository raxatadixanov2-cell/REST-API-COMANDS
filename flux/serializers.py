from rest_framework import serializers
from .models import FluxModel


class FluxSerializer(serializers.ModelSerializer):
    class Meta:
        model = FluxModel
        fields = ('title', 'description', 'created_at')
