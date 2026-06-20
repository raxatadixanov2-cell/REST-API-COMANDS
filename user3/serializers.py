from rest_framework import serializers
from .models import timeModel


class TimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = timeModel
        fields = ('id', 'name', 'surname')