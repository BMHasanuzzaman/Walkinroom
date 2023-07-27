from django.urls import path
from . import views

urlpatterns = [
    path('admin_home/', views.home_view, name='home'), 
]