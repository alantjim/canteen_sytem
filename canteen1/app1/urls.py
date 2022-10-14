from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index),
    path('home/', views.home),

    path('login/', views.login1),


    #path('staff/', views.staff),
    path('student/', views.student),
    path('profile/', views.profile),
    path('user1/', views.user1),

    path('logout/', views.logout),

    path('profile/login/', views.logout),
    path('cpass/', views.cpass),
    path('e_profile/', views.e_profile),

    path('e_profile/<int:id>/', views.e_profile),




]