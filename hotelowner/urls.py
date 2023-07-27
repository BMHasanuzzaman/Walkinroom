from django.urls import path
from . import views

urlpatterns = [
    path('hotelowner/', views.home_view, name='hotelowner_home'), 
]