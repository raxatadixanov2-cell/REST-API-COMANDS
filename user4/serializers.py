from rest_framework import serializers
from .models import canModel    

class CanSerializer(serializers.ModelSerializer):
    class Meta:
        model = canModel
        fields = ("id", "name", "surname", "age")