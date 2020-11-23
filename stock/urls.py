from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),   #localhost:8000/  the name is used for links
    path('about', views.about, name='about'),    #localhost:8000/about
]
