from rest_framework import serializers
from .models import EchoModel


class EchoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EchoModel
        fields = ('title', 'description', 'created_at')
