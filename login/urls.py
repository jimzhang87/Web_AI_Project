from django.urls import path,re_path
from . import views


urlpatterns = [
    re_path('login/', views.user_login),
    path('register/', views.register, name='register'),
    path('registration-success/', views.registration_success, name='registration_success'),
]
