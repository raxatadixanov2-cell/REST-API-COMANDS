from rest_framework.generics import ListAPIView,RetrieveAPIView,CreateAPIView,UpdateAPIView
from .models import canModel    
from .serializers import CanSerializer  

# Create your views here.
class CanListView(ListAPIView):
    queryset = canModel.objects.all()
    serializer_class = CanSerializer

class CanDetailView(RetrieveAPIView):
    queryset = canModel.objects.all()
    serializer_class = CanSerializer

class CanCreateView(CreateAPIView):
    queryset = canModel.objects.all()
    serializer_class = CanSerializer    

class CanUpdateView(UpdateAPIView):
    queryset = canModel.objects.all()
    serializer_class = CanSerializer    