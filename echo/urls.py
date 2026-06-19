from django.urls import path
from .views import EchoCreateView

urlpatterns = [
    path('echo/', EchoCreateView.as_view()),
]
