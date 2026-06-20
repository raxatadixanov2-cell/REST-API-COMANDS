from django.urls import path
from .views import SparkCreateView

urlpatterns = [
    path('spark/', SparkCreateView.as_view()),
]
