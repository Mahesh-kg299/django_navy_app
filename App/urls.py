from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view()),
    path('register/', views.RegisterView.as_view()),
    path('login/', views.LoginView.as_view()),
    path('logout/', views.LogoutView.as_view()),
    path('all/<item>/', views.ShowAllView.as_view()),
    path('add/<item>/', views.AddView.as_view()),
    path('set_armament/', views.SetArmamentView.as_view()),
]