#-*-coding: utf-8

from django.shortcuts import render
from board.api import TEST
import pandas as pd
from .form import StockForm

# Create your views here.

def add_stocks(request):
    return render(request, "add_stocks.html")




