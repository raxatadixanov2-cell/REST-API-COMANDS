from django.urls import path
from .views import FluxCreateView

urlpatterns = [
    path('flux/', FluxCreateView.as_view()),
]
