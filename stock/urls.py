from django.urls import path
from stock import views

urlpatterns = [
    
    path('stock/add_stocks/', views.add_stocks, name = 'add_stocks'),
    
    
]
