from rest_framework import serializers
from user1.models import apsModel
from .models import apsModel


class apsSerializer(serializers.ModelSerializer):
    class Meta:
        model = apsModel
        fields = ('id', 'name', 'surname')