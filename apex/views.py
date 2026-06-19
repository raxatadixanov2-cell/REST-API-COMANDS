from rest_framework.generics import CreateAPIView
from .serializers import ApexSerializer
from .models import ApexModel


class ApexCreateView(CreateAPIView):
    queryset = ApexModel.objects.all()
    serializer_class = ApexSerializer
