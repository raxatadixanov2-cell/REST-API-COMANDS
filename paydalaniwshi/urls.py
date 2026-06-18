from django.urls import path
from .views import (PaydalaniwshiAllView, PaydalaniwshiDetailView, PaydalaniwshiUpdateView,
                    PaydalaniwshiCreateView, PaydalaniwshiDeleteView)


urlpatterns = [
    path('all/', PaydalaniwshiAllView.as_view()),
    path('get/<int:pk>', PaydalaniwshiDetailView.as_view()),
    path('upd/<int:pk>', PaydalaniwshiUpdateView.as_view()),
    path('create/', PaydalaniwshiCreateView.as_view()),
    path('del/<int:pk>', PaydalaniwshiDeleteView.as_view())
]