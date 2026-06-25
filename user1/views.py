from rest_framework.generics import (ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView,
                                      DestroyAPIView, ListCreateAPIView, RetrieveUpdateAPIView,
                                        RetrieveUpdateDestroyAPIView,RetrieveDestroyAPIView)
from .models import dataModel
from .serializers import dataModelSerializer   


# Create your views here.
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

class dataAllCreateView(ListCreateAPIView):
    queryset = dataModel.objects.all()
    serializer_class = dataModelSerializer    


class dataDetailUpdateView(RetrieveUpdateAPIView):
    queryset = dataModel.objects.all()
    serializer_class = dataModelSerializer   

class dataDetailUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = dataModel.objects.all()
    serializer_class = dataModelSerializer   

class dataDetailDeleteView(RetrieveDestroyAPIView): 
    queryset = dataModel.objects.all()
    serializer_class = dataModelSerializer          


  


