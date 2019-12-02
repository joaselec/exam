#-*-coding: utf-8

from django.shortcuts import render
from board.api import TEST
import pandas as pd
from .form import StockForm

# Create your views here.

def stock(request):
    return render(request, "add_stock.html")

def add_stock(request):
    stock_name = request.GET.get('stock_name')
    purchase_price = request.GET.get('purchase_price')

    # stock_name = request.GET["stock_name"]
    # purchase_price = request.GET["purchase_price"]
    print(stock_name + purchase_price)

    return render(request, "add_stock.html")


