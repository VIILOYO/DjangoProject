from django.urls import path

from .views import RegisterPage, LogoutUser, LoginPage


urlpatterns = [
    path('register/', RegisterPage, name='register'),
    path('login/', LoginPage, name='login'),
    path('logout', LogoutUser, name='logout'),
]
