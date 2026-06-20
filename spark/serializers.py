from rest_framework import serializers
from .models import SparkModel


class SparkSerializer(serializers.ModelSerializer):
    class Meta:
        model = SparkModel
        fields = ('title', 'description', 'created_at')
