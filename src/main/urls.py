from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create-new/', views.create_new, name='create-new'),
    path('news/', views.news, name='news'),
]