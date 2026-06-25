from django.urls import path
from .views import (dataAllView, dataDetailView, dataCreateView,
                     dataUpdateView, dataDeleteView)  


urlpatterns = [
    path('all/', dataAllView.as_view()),
    path('detail/<int:pk>/', dataDetailView.as_view()),
    path('create/', dataCreateView.as_view()),
    path('update/<int:pk>/', dataUpdateView.as_view()),
    path('delete/<int:pk>/', dataDeleteView.as_view()),
]   