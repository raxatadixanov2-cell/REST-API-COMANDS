from rest_framework.generics import CreateAPIView
from .serializers import NovaSerializer
from .models import NovaModel


class NovaCreateView(CreateAPIView):
    queryset = NovaModel.objects.all()
    serializer_class = NovaSerializer
