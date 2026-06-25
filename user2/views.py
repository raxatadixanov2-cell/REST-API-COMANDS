from rest_framework.generics import (ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView)
from .models import dataModel
from .serializers import dataModelSerializer


class dataAllView(ListAPIView):
    queryset = dataModel.objects.all()
    serializer_class = dataModelSerializer

class dataDetailView(RetrieveAPIView):
    queryset = dataModel.objects.all()
    serializer_class = dataModelSerializer

class dataCreateView(CreateAPIView):
    queryset = dataModel.objects.all()
    serializer_class = dataModelSerializer    

class dataUpdateView(UpdateAPIView):
    queryset = dataModel.objects.all()
    serializer_class = dataModelSerializer

class dataDeleteView(DestroyAPIView):
    queryset = dataModel.objects.all()
    serializer_class = dataModelSerializer          