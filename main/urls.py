from venv import create
from xml.etree.ElementInclude import include
from django.urls import path
from . import views

app_name = "main"   


urlpatterns = [
#   path('',views.main, name ='main'),
#    path("", views.homepage, name="homepage"),
    path("register", views.register_request, name="register"),
    path('create/<str:pk>/', views.create, name='delete'),
]