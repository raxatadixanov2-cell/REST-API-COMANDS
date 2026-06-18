from django.shortcuts import render
from .models import UserModel
from .serializers import UserSerializer
from rest_framework.generics import (ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView,
                                     DestroyAPIView)


#all() - function
class UserAllview(ListAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer

#get() - function
class UserDetailView(RetrieveAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer

#create() - function
class UserCreateView(CreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer

#update() - function
class UserUpdateVIew(UpdateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer

#delete() - function
class UserDeleteView(DestroyAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer