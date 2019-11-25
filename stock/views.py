#-*-coding: utf-8

from django.shortcuts import render
from board.api import TEST
import pandas as pd
from .form import StockForm

# Create your views here.

def stock_main(request):   
    form = StockForm()
    context = {
        'form': form,
    }
    return render(request, "stock_main.html", context)

def stock(request):

    #code_df = pd.read_html('http://kind.krx.co.kr/corpgeneral/corpList.do?method=download&searchType=13', header=0)[0]
    code_df = pd.read_excel('test.xlsx')
    code_df.종목코드 = code_df.종목코드.map('{:06d}'.format)
    code_df = code_df[['회사명','종목코드']]
    code_df = code_df.rename(columns={'회사명':'name','종목코드':'code'})
    #code_df.head()
    item_name='신라젠' 
    url = get_url(item_name, code_df)

    df = pd.DataFrame()

    for page in range(1, 21): 
       pg_url = '{url}&page={page}'.format(url=url, page=page) 
       df = df.append(pd.read_html(pg_url, encoding="cp949", header=0)[0], ignore_index=True)
    #df = df.append(pd.read_html(url, encoding="cp949", header=0)[0], ignore_index=True)
    print(df)

    df = df.dropna()

    df.head()


    context = {
        
    }
    
    return render(request, "stock.html", context)

def get_url(item_name, code_df):
    code = code_df.query("name=='{}'".format(item_name))['code'].to_string(index=False)
    code = code[1:7]

    url = 'https://finance.naver.com/item/main.nhn?code={code}'.format(code=code)
    print("요청 URL = {}".format(url)) 
    return url




