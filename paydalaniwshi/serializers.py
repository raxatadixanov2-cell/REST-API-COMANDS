from rest_framework import serializers
from .models import PaydalaniwshiModel

class PaydalaniwshiSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaydalaniwshiModel
        fields = ('id', 'ati', 'fm')