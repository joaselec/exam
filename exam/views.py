from django.shortcuts import render
import sqlite3
import json
from django.core import serializers
from django.http import HttpResponse, JsonResponse


def getExample(request):
    conn = sqlite3.connect("first.db")
    cur = conn.cursor()
    cur.execute("""
                    SELECT id, content FROM TB_EXAM ORDER BY RANDOM() LIMIT 1
                """)
    row = cur.fetchone()
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
        "exam_content": exam_content,
    }

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

    

   




