from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create-new/', views.create_new, name='create-new'),
    path('news/', views.news, name='news'),
    path('update-new/<int:pk>/', views.update_new, name='update-new'),
    path('delete-new/<int:pk>/', views.delete_new, name='delete-new'),
    path('create-category/', views.create_category, name='create-category'),
]