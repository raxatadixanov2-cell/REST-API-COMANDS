from rest_framework.generics import CreateAPIView
from .serializers import SparkSerializer
from .models import SparkModel


class SparkCreateView(CreateAPIView):
    queryset = SparkModel.objects.all()
    serializer_class = SparkSerializer
