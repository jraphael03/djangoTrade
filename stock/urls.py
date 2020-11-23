from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),   #localhost:8000/
]
