from rest_framework.generics import CreateAPIView
from .serializers import FluxSerializer
from .models import FluxModel


class FluxCreateView(CreateAPIView):
    queryset = FluxModel.objects.all()
    serializer_class = FluxSerializer
