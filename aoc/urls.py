from unicodedata import name
from django.urls import path
from . import views
#from django.contrib.auth.urls import url
from django.contrib import admin
from .views import createpost, detail_post_view, postpreference

urlpatterns = [
  #  path('pics/', views.pics, name='pics'),
  #  path('index/' views.index, name='index')
    path('home/', views.home, name='home'),

    path('', views.createpost, name='createpost'),
    path('detail/', views.detail_post_view, name='detail'),
    path('postpreference/',views.postpreference, name='postpreference'),
]