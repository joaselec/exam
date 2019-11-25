from django.urls import path
from stock import views

urlpatterns = [
    
    path('stock/stock/', views.stock, name = 'stock'),
    path('stock/', views.stock_main, name = 'stock_main'),
    
]
