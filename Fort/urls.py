from django.contrib import admin
from django.urls import path 
from.views import Login ,test_view
urlpatterns =[
    path('admin/', admin.site.urls),
    path('login/',Login),
    path('', test_view),
]