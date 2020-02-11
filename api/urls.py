from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [ 
    path('get_currency/',views.get_currency,name='get_currency'),
    path('provider/',views.provider_view,name='provider_view'),
]