from django.urls import path
from .views import SignUpPage

urlpatterns = [
    path('signup/', SignUpPage, name='signup'),
    # ... other URL patterns ...
]
