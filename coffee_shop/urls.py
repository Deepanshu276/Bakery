from django.urls import path
from coffee_shop import views

urlpatterns = [
    path('', views.home, name="home")
]
