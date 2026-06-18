from django.urls import path
from .views import OqiwshiAllView, OqiwshiDetailUpdateDeleteView

urlpatterns = [
    path('all/', OqiwshiAllView.as_view()),
    path('sulayman/<int:pk>', OqiwshiDetailUpdateDeleteView.as_view())
]