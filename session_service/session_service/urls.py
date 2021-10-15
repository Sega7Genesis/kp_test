from django.urls import path

from . import views

urlpatterns = [
    path('auth', views.LoginView.as_view(), name='auth'),
    path('verify', views.VerifyView.as_view(), name='verify'),
    path('users', views.UsersView.as_view(), name='users'),
]