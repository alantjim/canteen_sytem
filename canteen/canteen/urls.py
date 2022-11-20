"""canteen1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

import document as document
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from django.conf import settings



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app1.urls')),
    path('home/', include('app1.urls')),


    path('login/', include('app1.urls')),
    #path('staff/', include('app1.urls')),
    path('student/', include('app1.urls')),
    path('/profile/', include('app1.urls')),
    path('user1/', include('app1.urls')),
    path('shop/', include('app1.urls')),
    path('user_search/', include('app1.urls')),
    path('shop1/<int:id>', include('app1.urls')),
    path('paymentdone/', include('app1.urls')),
    path('u_orders/', include('app1.urls')),
    path('/staff_item_add/', include('app1.urls')),
    path('/staff_item_view/', include('app1.urls')),
    path('/staff_item_edit/<int:id/', include('app1.urls')),
    path('/staff_order_view/', include('app1.urls')),



    path('/logout/', include('app1.urls')),
    #path('user1/logout/', include('app1.urls')),
    #path('user1/profile/logout/', include('app1.urls')),

    path('profile/login/', include('app1.urls')),
    path('/cpass/', include('app1.urls')),
    #path('/e_profile/', include('app1.urls')),
    path('/e_profile/', include('app1.urls')),
    path('/u_cart/', include('app1.urls')),
    path('/icart/<int:id>/', include('app1.urls')),
    path('/de_cart/<int:id>/', include('app1.urls')),
    path('staff_dash/', include('app1.urls')),

    path('cart/', include('app1.urls')),
    path('checkout/', include('app1.urls')),



] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


