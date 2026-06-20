from rest_framework.generics import CreateAPIView
from .serializers import EchoSerializer
from .models import EchoModel


class EchoCreateView(CreateAPIView):
    queryset = EchoModel.objects.all()
    serializer_class = EchoSerializer
