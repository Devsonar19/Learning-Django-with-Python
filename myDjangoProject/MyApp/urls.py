from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('countWord', views.countWord, name='countWord'),
    path('register', views.register, name='register'),
]