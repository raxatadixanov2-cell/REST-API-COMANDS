from rest_framework.generics import ListAPIView,RetrieveAPIView,CreateAPIView,UpdateAPIView
from .models import timeModel
from .serializers import TimeSerializer

# Create your views here.


class TimeListView(ListAPIView):
    queryset = timeModel.objects.all()
    serializer_class = TimeSerializer

class TimeDetailView(RetrieveAPIView):
    queryset = timeModel.objects.all()
    serializer_class = TimeSerializer    

class TimeCreateView(CreateAPIView):
    queryset = timeModel.objects.all()
    serializer_class = TimeSerializer   

class TimeUpdateView(UpdateAPIView):
    queryset = timeModel.objects.all()
    serializer_class = TimeSerializer    

    