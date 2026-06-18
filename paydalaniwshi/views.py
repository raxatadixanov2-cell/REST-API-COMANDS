from django.shortcuts import render
from .models import PaydalaniwshiModel
from .serializers import PaydalaniwshiSerializer
from rest_framework.generics import (ListAPIView, RetrieveAPIView, UpdateAPIView,
                                     CreateAPIView, DestroyAPIView)


class PaydalaniwshiAllView(ListAPIView):
    queryset = PaydalaniwshiModel.objects.all()
    serializer_class = PaydalaniwshiSerializer



class PaydalaniwshiDetailView(RetrieveAPIView):
    queryset = PaydalaniwshiModel.objects.all()
    serializer_class = PaydalaniwshiSerializer


class PaydalaniwshiUpdateView(UpdateAPIView):
    queryset = PaydalaniwshiModel.objects.all()
    serializer_class = PaydalaniwshiSerializer


class PaydalaniwshiCreateView(CreateAPIView):
    queryset = PaydalaniwshiModel.objects.all()
    serializer_class = PaydalaniwshiSerializer


class PaydalaniwshiDeleteView(DestroyAPIView):
    queryset = PaydalaniwshiModel.objects.all()
    serializer_class = PaydalaniwshiSerializer