"""
URL configuration for untitled project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path

from OnlineDressShop import views

urlpatterns = [
    # path('admin/', admin.site.urls)
    path('',views.log),
    path('log_post',views.log_post),
    path('admin_home',views.admin_home),
    path('user_home', views.user_home),

    path('add_dress',views.add_dress),
    path('add_dress_post',views.add_dress_post),


    path('dress_categoryadd',views.dress_categoryadd),
    path('dress_categoryadd_post',views.dress_categoryadd_post),

    path('dress_categoryedit/<id>',views.dress_categoryedit),
    path('dress_categoryedit_post/<id>',views.dress_categoryedit_post),

    path('dress_category_delete/<id>',views.dress_category_delete),

    path('dress_categoryview',views.dress_categoryview),

    path('editdress/<id>',views.editdress),
    path('editdress_post/<id>',views.editdress_post),
    path('dress_delete/<id>',views.dress_delete),
    path('view_order',views.view_order),
    path('orderd_item/<id>',views.orderd_item),
    path('view_rating',views.view_rating),
    path('viewdress',views.viewdress),
    path('change_password',views.change_password),
    path('change_password_post',views.change_password_post),
    path('registeration',views.registeration),
    path('registration_post',views.registration_post),
    path('viewdressuser',views.viewdressuser),
    path('addtocart/<id>',views.addtocart),
    path('addtocart_post/<i>',views.addtocart_post),
    path('viewcart',views.viewcart),
    path('delete_cartitem/<id>',views.delete_cartitem),
    path('orderbyuseraddress/<am>',views.orderbyuseraddress),
    path('orderbyuseraddress_post/<am>',views.orderbyuseraddress_post),
    path('orderchoose_post/<am>/<oid>',views.orderchoose_post),
    path('orderbank/<am>/<oid>',views.orderbank),

    path('changepassword',views.changepassword),
    path('changepassword_post',views.changepassword_post),
    path('viewprofile',views.viewprofile),
    path('vieworder',views.vieworder),
    path('orderitems/<id>',views.orderitems),
    path('previoushistory',views.previoushistory),
    path('rate/<id>',views.rate),
    path('rate_post/<id>',views.rate_post),
    path('logout',views.logout)
]
