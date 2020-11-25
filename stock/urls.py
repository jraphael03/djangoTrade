from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),   #localhost:8000/  the name is used for links
    path('about', views.about, name='about'),    #localhost:8000/about
    path('add_stock.html', views.add_stock, name='add_stock'),
    path('delete/<stock_id>', views.delete, name='delete'),
    path('delete_stock.html', views.delete_stock, name="delete_stock"),
]
