from django.urls import path
from stock import views

urlpatterns = [
    
    path('stock/stock/', views.stock, name = 'stock'),
    path('stock/add_stock/', views.add_stock, name = 'add_stock'),
    
    
]
