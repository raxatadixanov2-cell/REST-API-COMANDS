from django.contrib import path
from .views import TimeCreateView, TimeDetailView, TimeListView, TimeUpdateView  


urlpatterns = [
    path('time/', TimeListView.as_view(), name='time-list'),
    path('time/<int:pk>/', TimeDetailView.as_view(), name='time-detail'),
    path('time/create/', TimeCreateView.as_view(), name='time-create'),
    path('time/<int:pk>/update/', TimeUpdateView.as_view(), name='time-update'),
]   