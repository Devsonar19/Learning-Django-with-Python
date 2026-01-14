from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('countWord', views.countWord, name='countWord'),
    path('register', views.register, name='register'),
    path('login', views.login_view, name='login'),
    # path('logout', views.logout_view, name='logout'),
    path('post/<str:pk>', views.post, name='post'),
]