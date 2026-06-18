from django.shortcuts import render
from .models import HammesiModel
from .serializers import HammesiSerializer
from rest_framework.generics import (ListAPIView, RetrieveAPIView, UpdateAPIView,
                                     CreateAPIView, DestroyAPIView)


class HammesiAllView(ListAPIView):
    queryset = HammesiModel.objects.all()
    serializer_class = HammesiSerializer

class HammesiDetailview(RetrieveAPIView):
    queryset = HammesiModel.objects.all()
    serializer_class = HammesiSerializer


class HammesiUpdateView(UpdateAPIView):
    queryset = HammesiModel.objects.all()
    serializer_class = HammesiSerializer


class HammesiCreateView(CreateAPIView):
    queryset = HammesiModel.objects.all()
    serializer_class = HammesiSerializer

class HammesiDeleteView(DestroyAPIView):
    queryset = HammesiModel.objects.all()
    serializer_class = HammesiSerializer

