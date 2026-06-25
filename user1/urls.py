from django.urls import path
from .views import(
    dataAllCreateView,
    dataAllView,
    dataCreateView,
    dataDeleteView,
    dataDetailDeleteView,
    dataDetailUpdateDeleteView,
    dataDetailUpdateView,
    dataDetailView,
    dataUpdateView,

)
urlpatterns = [
    path('all/', dataAllView.as_view()),
    path('detail/<int:pk>/', dataDetailView.as_view()),
    path('create/', dataCreateView.as_view()),
    path('update/<int:pk>/', dataUpdateView.as_view()),
    path('delete/<int:pk>/', dataDeleteView.as_view()),
    path('allcreate/', dataAllCreateView.as_view()),
    path('detailupdate/<int:pk>/', dataDetailUpdateView.as_view()),
    path('detailupdatedelete/<int:pk>/', dataDetailUpdateDeleteView.as_view()),
    path('detaildelete/<int:pk>/', dataDetailDeleteView.as_view()),
    
]