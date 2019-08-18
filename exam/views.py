from django.shortcuts import render
import sqlite3
import json
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from exam.models import result
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def statics(request):
    
    user_name = request.user.username
    conn = sqlite3.connect("first.db")
    cur = conn.cursor()
    sql = "select title_id, name, count(*) as cnt from (select a.title_id, b.name from exam_result a, TB_TITLE b where a.user_name = ? and a.title_id=b.id and a.check_yn = 'N') group by title_id order by cnt DESC"
    cur.execute(sql, (user_name,))
    statics_list = cur.fetchall()
    size = 10
    paginator = Paginator(statics_list,size)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    #statics = json.dumps(statics_list)
    context = {
        #"test" : statics_list,
        "posts" : posts,
        #"statics" : statics,
    }
    return render(request, "statics.html", context)
    

def getExample(request):
    try: 
        conn = sqlite3.connect("first.db")
        cur = conn.cursor()
        sql = """
                SELECT id, content 
                FROM TB_EXAM 
                WHERE id not in (
                    select distinct example_id 
                    from exam_result
                    where session_id = ?
                    and check_yn = 'Y'
                    )
                ORDER BY RANDOM() LIMIT 1
              """
        cur.execute(sql, (request.session.session_key,))
        row = cur.fetchone()
        example_id = row[0]
        title_id = row[0][0:5]
        #length = len(title_id)
        if title_id[4] == ".": 
            title_id = row[0][0:6]

        exam_content = row[1]
        sql = "SELECT name, content FROM TB_TITLE WHERE id = ?"
        cur.execute(sql, (title_id,))
        row = cur.fetchone()
        title_name = row[0]
        title_content = row[1]

        #cur.execute("SELECT content FROM TB_TITLE WHERE id = ?",(title_id))
                    
        context = {
            "title_id": title_id,
            "title_name": title_name,
            #"title_id": "2.1.1",
            "title_content": title_content,
            "example_id": example_id,
            "example_content": exam_content,
        }

    finally:
        conn.close()

    return render(request, "exam.html", context)


def getTitleContent(request):
    try:
        title_id = request.GET["title_id"]
        conn = sqlite3.connect("first.db")
        cur = conn.cursor()
        cur.execute("SELECT name, content FROM TB_TITLE WHERE id = ?",(title_id,))
        row = cur.fetchone()
        name = row[0]
        content = row[1]
        return JsonResponse({
            "false_title_name" : name,
            "false_title_content" : content,
        }, json_dumps_params = {'ensure_ascii': True})
    #except:

    finally:
        conn.close()



def sendResult(request):
    #try:
    select_id = request.GET["select_id"]
    example_id = request.GET["example_id"]
    session_id = request.session.session_key
    user_name = request.user.username
    date = request.user.last_login.strftime('%Y%m%d')
    if example_id[5] != ".": 
        title_id = example_id[0:6]
    else:
        title_id = example_id[0:5]

    if select_id == title_id :
        check_yn = 'Y'
    else :
        check_yn = 'N'
    
    result(select_id=select_id, title_id = title_id, example_id=example_id, session_id=session_id, user_name=user_name, date=date, check_yn=check_yn).save()
    return JsonResponse({
    }, json_dumps_params = {'ensure_ascii': True})
    # finally:
    #     conn.close()