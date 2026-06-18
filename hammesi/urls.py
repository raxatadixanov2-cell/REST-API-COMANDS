from django.urls import path
from .views import (HammesiAllView, HammesiDetailview, HammesiUpdateView, HammesiCreateView,
                    HammesiDeleteView)


urlpatterns = [
    path('all/', HammesiAllView.as_view()),
    path('get/<int:pk>', HammesiDetailview.as_view()),
    path('update/<int:pk>', HammesiUpdateView.as_view()),
    path('create/', HammesiCreateView.as_view()),
    path('del/<int:pk>', HammesiDeleteView.as_view())
]