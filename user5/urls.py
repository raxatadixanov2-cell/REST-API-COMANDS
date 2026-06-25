from django.urls import path
from .views import CanListView, CanDetailView, CanCreateView, CanUpdateView     



urlpatterns = [
    path('can/', CanListView.as_view(), name='can-list'),  
    path('can/<int:pk>/', CanDetailView.as_view(), name='can-detail'),
    path('can/create/', CanCreateView.as_view(), name='can-create'),
    path('can/<int:pk>/update/', CanUpdateView.as_view(), name='can-update'),
]   