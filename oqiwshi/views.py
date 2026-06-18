from django.shortcuts import render
from .models import OqiwshiModel
from .serializers import OqiwshiSerializer
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView



class OqiwshiAllView(ListAPIView):
    queryset = OqiwshiModel.objects.all()
    serializer_class = OqiwshiSerializer


class OqiwshiDetailUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = OqiwshiModel.objects.all()
    serializer_class = OqiwshiSerializer

