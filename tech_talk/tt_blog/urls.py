from django.urls import path

from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('upload_photo/', views.upload_photo, name='upload_photo'),
    path('photo/<int:pk>/', views.photo_detail, name='photo_detail'),
]