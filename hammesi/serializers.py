from rest_framework import serializers
from .models import HammesiModel


class HammesiSerializer(serializers.ModelSerializer):
    class Meta:
        model = HammesiModel
        fields = ('id', 'name', 'surname', 'age')