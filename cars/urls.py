

from cars import views
from django.contrib import admin
from django.urls import include, path


urlpatterns = [

    path('cars', views.cars, name='cars'),
    
] 


