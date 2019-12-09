#-*- coding:utf-8 -*-

from django.shortcuts import render
from board.api import TEST
import pandas as pd
from .form import StockForm
from stock.models import *
from stock.cron import *
from django.http import HttpResponse, JsonResponse




# Create your views here.


def stock(request):
    try:
        conn = sqlite3.connect("first.db")
        cur = conn.cursor()
        sql = "select * from stock_stocks"
        cur.execute(sql)
        posts = cur.fetchall()

        context = {        
            "posts" : posts,        
        }
    finally:
        conn.close()
    
    return render(request, "add_stock.html", context)

def add_stock(request):
    try: 

        stock_name = request.GET.get('stock_name').decode('cp949').encode('utf-8')

        print(stock_name)
        
        purchase_price = request.GET.get('purchase_price')

        conn = sqlite3.connect("first.db")
        cur = conn.cursor()

        if check_duplicate(stock_name):
            return JsonResponse({
                "msg" : '중복 데이터 입력입니다.',
                }, json_dumps_params = {'ensure_ascii': True})

        code = get_code(stock_name)

        if code == 0:
            return JsonResponse({
                "msg" : '잘못된 종목명입니다.',
            }, json_dumps_params = {'ensure_ascii': True})


       
        sql = """
            insert into stock_stocks(stock_code, stock_name, start_price)
            values(?,?,?)
        """

        cur.execute(sql,(code, stock_name, purchase_price))
        conn.commit()

        test()
    finally:
        conn.close()
    return render(request, "add_stock.html")

def check_duplicate(stock_name):
    try:
        conn = sqlite3.connect("first.db")
        cur = conn.cursor()
        sql = "select count(stock_code) from stock_stocks where stock_name = ?"

        cur.execute(sql,(stock_name,))

        count = cur.fetchone()

        if count[0] == 0:
            return False
        else:
            return True

    finally:
        conn.close()



