from django.urls import path
from .views import NovaCreateView

urlpatterns = [
    path('nova/', NovaCreateView.as_view()),
]
