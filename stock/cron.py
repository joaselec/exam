#from stock.models import CronLog
import os
from datetime import datetime
import pandas_datareader.data as wb
import pandas as pd
import requests
import json
import pandas as pd
import time
import sqlite3
import telepot

def get_price(code):
    # DATA를 불러오는 부분 입니다.
    url = 'http://finance.daum.net/api/charts/A%s/days?limit=1&adjusted=true'%(code)
    headers = {
                'Accept': 'application/json, text/plain, */*',
                'Accept-Encoding': 'gzip, deflate',
                'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
                'Connection': 'keep-alive',
                'Cookie': 'GS_font_Name_no=0; GS_font_size=16; _ga=GA1.3.937989519.1493034297; webid=bb619e03ecbf4672b8d38a3fcedc3f8c; _ga=GA1.2.937989519.1493034297; _gid=GA1.2.215330840.1541556419; KAKAO_STOCK_RECENT=[%22A069500%22]; recentMenus=[{%22destination%22:%22chart%22%2C%22title%22:%22%EC%B0%A8%ED%8A%B8%22}%2C{%22destination%22:%22current%22%2C%22title%22:%22%ED%98%84%EC%9E%AC%EA%B0%80%22}]; TIARA=C-Tax5zAJ3L1CwQFDxYNxe-9yt4xuvAcw3IjfDg6hlCbJ_KXLZZhwEPhrMuSc5Rv1oty5obaYZzBQS5Du9ne5x7XZds-vHVF; webid_sync=1541565778037; _gat_gtag_UA_128578811_1=1; _dfs=VFlXMkVwUGJENlVvc1B3V2NaV1pFdHhpNTVZdnRZTWFZQWZwTzBPYWRxMFNVL3VrODRLY1VlbXI0dHhBZlJzcE03SS9Vblh0U2p2L2V2b3hQbU5mNlE9PS0tcGI2aXQrZ21qY0hFbzJ0S1hkaEhrZz09--6eba3111e6ac36d893bbc58439d2a3e0304c7cf3',
                'Host': 'finance.daum.net',
                'If-None-Match': 'W/"23501689faaaf24452ece4a039a904fd"',
                'Referer': 'http://finance.daum.net/quotes/A069500',
                'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
                }
    headers['Referer'] = 'http://finance.daum.net/quotes/A%s'%code
    r = requests.get(url, headers = headers)
    r.encoding = 'utf-8'
    # DATA를 보기 좋게 편집하는 부분 입니다.
    data = json.loads(r.text)
    df = pd.DataFrame(data['data'])
    #df.index = pd.to_datetime(df['candleTime'])    
    return df

def get_code(name):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filepath = os.path.join(BASE_DIR, 'company_code.xlsx')
    filename = os.path.basename(filepath)

    df = pd.read_excel(filename)
    cd = df["회사명"] == name
    h = df.loc[cd,"종목코드"]
    if h.empty:
        return 0
    code = h.to_string(index = False)
    if code[0] == ' ':
        if len(code) == 5:
            code = code[1:5]
            code = '00' + code
        elif len(code) == 6:
            code = code[1:6]
            code = '0' + code
        elif len(code) == 7:
            code = code[1:7]

    
    return code

def load_stocks():
    try:
        stock_list = []
        conn = sqlite3.connect("first.db")
        cur = conn.cursor()
        cur.execute("SELECT stock_code FROM stock_stocks")
        rows = cur.fetchall()
        for row in rows:
            stock_list.append(row[0])
        return stock_list
    finally:
        conn.close()
    return 

def set_current_prices(stock_list):
    try:
        conn = sqlite3.connect("first.db")
        cur = conn.cursor()
        #sql = ""
        for code in stock_list:
            k = get_price(code)
            current_price = k["tradePrice"].to_string(index = False)
            return_rate = get_returns(current_price, code)
            update_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            sql = "update stock_stocks set current_price = (?), stock_returns = (?), update_date = (?) where stock_code = (?);"
            cur.execute(sql,(str(current_price), str(return_rate), update_date, code))
            conn.commit()

    finally:
        conn.close()

def get_returns(current_price, code):
    try:
        conn = sqlite3.connect("first.db")
        cur = conn.cursor()
        #sql = ""
        #for code in stock_list:
        # k = get_price(code)
        # current_price = float(k["tradePrice"].to_string(index = False))

        sql = "select start_price from stock_stocks where stock_code = ?"
        cur.execute(sql, (code,))              
        row = cur.fetchone()
        sp = int(row[0])
        deff = float(current_price) - sp
        return_rate = round(deff / sp * 100)
        
        return return_rate

    finally:
        conn.close()

def check_price():
    try:        
        conn = sqlite3.connect("first.db")
        cur = conn.cursor()

        # query = cur.execute("select * from stock_stocks")
        # cols = [column[0] for column in query.description]
        # df = pd.DataFrame.from_records(data=query.fetchall(), columns=cols)

        # df['_date'] = df['date'].str.slice(0,10)
        # con_right = (df['check_yn'] == 'Y') & (df['user_name'] == user_name)
        # con_all = df['user_name'] == user_name

        # grouped_right = df.loc[con_right,"check_yn"].groupby(df["_date"]).count()
        # grouped_all = df.loc[con_all,"check_yn"].groupby(df["_date"]).count()
        # right_rate = grouped_right / grouped_all 
        # right_rate = pd.DataFrame({'dates':right_rate.index, 'rates':right_rate.values, 'cnts':grouped_all.values}).fillna(0)
        # right_rate['rates'] = round(right_rate['rates'] * 100)
        # dates = []
        # rates = []
        # cnts = []
        # #dates.append('날짜')
        # dates = right_rate['dates'].values.tolist()

        # #rates.append('정답률')
        # rates = right_rate['rates'].values.tolist()
        # #count 
        # cnts = right_rate['cnts'].values.tolist()

        # data = {
        #     'column':[
        #         dates,
        #         rates,
        #         cnts,
        #     ],
        # }

    finally:
        conn.close()

def test():
    rows = load_stocks()
    set_current_prices(rows)

rows = load_stocks()
set_current_prices(rows)


# def get_code_db():
#     conn = sqlite3.connect("first.db")
#     cur = conn.cursor()
#     sql = "select stock_name from "

# # def send_telegram(msg):
# #     token = "913353921:AAF2jBq2Uj_6NzCyPQHxiikll3Uv8Bd83mg"
# #     mc = "861046322"
# #     #mc = "919725238"
# #     bot = telepot.Bot(token)
# #     bot.sendMessage(mc, msg)

# l = list()

# last_price = float(0.0)

# while 1:
#     dt = datetime.datetime.now()
#     c = get_code('삼성전자')
#     k = get_price(c,1)
#     current_price = float(k["tradePrice"].to_string(index = False))
#     if last_price > current_price:
#         print("하락 " + str(last_price) + " " + str(current_price))
#         #send_telegram("하락 " + str(last_price) + " " + str(current_price)) 
#     elif last_price == current_price:
#         print("유지 " + str(last_price) + " " + str(current_price))
#         #send_telegram("유지 " + str(last_price) + " " + str(current_price))
#     else:
#         print("상승 " + str(last_price) + " " + str(current_price))
#         #send_telegram("상승 " + str(last_price) + " " + str(current_price))

#     last_price = current_price
#     l.insert(0,[str(dt),c,k["tradePrice"].to_string(index = False)])
#     time.sleep(10)


# fileRW()
# #my_scheduled_job()