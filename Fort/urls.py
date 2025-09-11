from django.contrib import admin
from django.urls import path 
from.views import Login 
urlpatterns =[
    path('login',Login),
    path('', test_view),
]