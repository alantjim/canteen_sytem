from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index),
    # path('home/', views.home),

    path('login/', views.login1),


    #path('staff/', views.staff),
    path('student/', views.student),
    path('profile/', views.profile),
    path('user1/', views.user1),
    path('shop/', views.shop),
    path('user_search/', views.user_search),

    path('shop1/<int:id>', views.shop1),
    path('staff_dash/', views.staff_dash),

    path('staff_item_add/', views.staff_item_add),
    path('staff_item_view/', views.staff_item_view),
    path('cart/', views.cart),
    path('checkout/', views.checkout),

    path('logout/', views.logout),

    path('profile/login/', views.logout),
    path('cpass/', views.cpass),
   # path('e_profile/', views.e_profile),

    path('e_profile/', views.e_profile),
    path('icart/<int:id>/', views.add_cart_i),

    path('de_cart/<int:id>/', views.de_cart),
    path('u_cart/', views.u_cart),




]