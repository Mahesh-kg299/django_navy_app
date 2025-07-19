from django.urls import path
from . import views

urlpatterns = [
    path('ac_class/', views.AircraftCarrierClassListView.as_view()),
    path('ac/', views.AircraftCarrierListView.as_view()),
    path('armament/', views.ArmamentListView.as_view()),
    path('builder/', views.BuilderListView.as_view()),
    path('armament/<pk>/', views.ArmamentDetailView.as_view()),
    path('class_armament/', views.ACClassArmamentListView.as_view()),
    path('class_armament/<pk>/', views.ACClassArmamentDetailView.as_view()),
]