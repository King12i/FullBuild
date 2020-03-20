from django.urls import path
from . import views

urlpatterns = [
    # Path and route for displaying forms for login/registration
    path('', views.logreg),
    
    # Path and route for processing submitted registration form
    path('register', views.register),
    
    # Path and route for processing submitted login form
    path('login', views.login),

    # Path and route for logging out a user
    path('logout', views.logout)
]