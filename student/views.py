from django.shortcuts import render
from .models import StudentModel
from .serializers import StudentSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView



class StudentAllCreateView(ListCreateAPIView):
    queryset = StudentModel.objects.all()
    serializer_class = StudentSerializer



class StudentDetailUpdateView(RetrieveUpdateAPIView):
    queryset = StudentModel.objects.all()
    serializer_class = StudentSerializer

class StudentDetailDeleteView(RetrieveDestroyAPIView):
    queryset = StudentModel.objects.all()
    serializer_class = StudentSerializer