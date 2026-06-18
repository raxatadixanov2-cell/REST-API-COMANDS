from rest_framework import serializers
from .models import OqiwshiModel

class OqiwshiSerializer(serializers.ModelSerializer):
    class Meta:
        model = OqiwshiModel
        fields = ('id', 'name', 'username', 'age')