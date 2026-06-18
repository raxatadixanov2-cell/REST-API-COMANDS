from django.urls import path
from .views import (UserAllview, UserDetailView, UserCreateView, UserUpdateVIew,
                    UserDeleteView)

urlpatterns = [
    path('all/', UserAllview.as_view()),
    path('get/<int:pk>', UserDetailView.as_view()),
    path('create/', UserCreateView.as_view()),
    path('update/<int:pk>', UserUpdateVIew.as_view()),
    path('delete/<int:pk>', UserDeleteView.as_view())
]