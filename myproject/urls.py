# myproject/urls.py

from django.contrib import admin
from django.urls import path, include
from . import views  # Import the views module from the main project folder

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name='home'),  # Make sure the URL pattern is named 'home'
    path('accounts/', include('accounts.urls')),
    
]
