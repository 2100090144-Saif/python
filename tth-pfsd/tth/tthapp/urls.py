from django.urls import path, include
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.function1, name='home'),
    path('klu2/', views.home),
    # path('time/', views.function2),
    # path('temp1/', views.city),
    # path('temp1/temp2/', views.temp),
    # path('qrcode1/', views.qrcode1),
    # path('qrcode12/',views.qrcode12, name='qrcode1'),
    path('link3/',views.function3, name='contact'),
    path('contactus/',views.contactus1, name='contactus'),
    path('registeruser/',views.registeruser, name='reguser'),
    path('register/',views.register, name='register1'),
    path('loginuser/',views.loginuser,name='loginu'),
    path('login/',views.loggedin,name='login')
]


