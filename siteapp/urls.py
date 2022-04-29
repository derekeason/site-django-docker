from django.urls import path
from siteapp import views

urlpatterns = [
    path('', views.index, name='index'),
]
