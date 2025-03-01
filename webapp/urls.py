
from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),
    path('service/', views.service, name='service'),
    path('servicesignup/', views.servicesignup, name='servicesignup'),
    path('addpoi/', views.addpoi, name='addpoi'),
    path('servicelogin/', views.servicelogin, name='servicelogin'),
    path('shome/', views.shome, name='shome'),
    path('slogout/', views.slogout, name='slogout'),
    path('viewev/', views.viewev, name='viewev'),
    path('editdata/', views.editdata, name='editdata'),
    path('updatedata/', views.updatedata, name='updatedata'),

    path('usersignup/', views.usersignup, name='usersignup'),
    path('signupstore/', views.signupstore, name='signupstore'),
    path('userlogin/', views.userlogin, name='userlogin'),

    path('uhome/', views.uhome, name='uhome'),
    path('ulogout/', views.ulogout, name='ulogout'),
    path('viewprofile/', views.viewprofile, name='viewprofile'),

    path('locationset/', views.locationset, name='locationset'),
    path('getdata/', views.getdata, name='getdata'),
    path('viewloc2/', views.viewloc2, name='viewloc2'),
    path('search/', views.search, name='search'),
    



]
