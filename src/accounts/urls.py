from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_user, name='register'),
    path('users/', views.users, name='users'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout')
]