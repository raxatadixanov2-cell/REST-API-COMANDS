from rest_framework import serializers
from .models import NovaModel


class NovaSerializer(serializers.ModelSerializer):
    class Meta:
        model = NovaModel
        fields = ('title', 'description', 'created_at')
