from rest_framework import serializers
from .models import dataModel



class dataModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = dataModel
        fields = ('id', 'name', 'surname', 'age')