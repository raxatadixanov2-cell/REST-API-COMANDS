from django.urls import path
from .views import StudentAllCreateView, StudentDetailUpdateView, StudentDetailDeleteView

urlpatterns = [
    path('rxt/', StudentAllCreateView.as_view()),
    path('bxm/<int:pk>', StudentDetailUpdateView.as_view()),
    path('ix/<int:pk>', StudentDetailDeleteView.as_view())
]
