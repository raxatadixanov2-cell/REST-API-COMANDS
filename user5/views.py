from rest_framework.generics import DestroyAPIView, ListAPIView,RetrieveAPIView,CreateAPIView,UpdateAPIView
from .models import  PostModel    
from .serializers import Serializer     

# Create your views here.



class PostListView(ListAPIView):
    queryset = PostModel.objects.all()
    serializer_class = Serializer  


class PostDetailView(RetrieveAPIView):
    queryset = PostModel.objects.all()
    serializer_class = Serializer   

class PostCreateView(CreateAPIView):
    queryset = PostModel.objects.all()
    serializer_class = Serializer   


class PostUpdateView(UpdateAPIView):
    queryset = PostModel.objects.all()
    serializer_class = Serializer   

class PostDeleteView(DestroyAPIView):
    queryset = PostModel.objects.all()
    serializer_class = Serializer                  


