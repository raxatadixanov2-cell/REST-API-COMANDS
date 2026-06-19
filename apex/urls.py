from django.urls import path
from .views import ApexCreateView

urlpatterns = [
    path('apex/', ApexCreateView.as_view()),
]
