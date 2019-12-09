from django.shortcuts import render, redirect
import sqlite3
import json
import openpyxl
import os
from django.core import serializers
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils import timezone
from django.db import transaction
from datetime import datetime
import logging
from django.contrib.auth.models import Permission, User
from django.shortcuts import get_object_or_404
from board.models import board
from django.urls import reverse
from .form import BoardForm
#from .api import TEST



logger = logging.getLogger(__name__)

def board_new(request):
    form = BoardForm()
    context = {
        'form': form,
    }
    return render(request, "board_new.html", context)


def board_list(request):
    try:

        #boardList = board.objects.all()
        
        boardList = board.objects.filter(enable_yn='y')

        size = 10
        paginator = Paginator(boardList,size)
        page = request.GET.get('page')
        posts = paginator.get_page(page)
        context = {
            "posts" : posts,
        }
    except Exception as ex:
        print(ex.__str__)
    # finally:
    #     print("finish")
    return render(request, "board_list.html", context)

def board_modify(request, id):
    boardDetail = board.objects.get(pk=id) 
    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            #board(username=username, title = title, detail=detail, write_date = datetime.now().strftime('%Y%m%d')).save() 
            print(form.cleaned_data)
            boardDetail.title = form.cleaned_data['title']
            boardDetail.detail = form.cleaned_data['detail']
            boardDetail.modify_date = datetime.now().strftime('%Y%m%d')
            boardDetail.save()
            url = '/board/detail/'+str(boardDetail.id)+'/'
            return redirect(url)
    else: 
        form = BoardForm(instance = boardDetail)
        context = {
            'form': form,
            'writing': True,
            'now': 'edit',
            'id': id,
        }
        return render(request, "board_modify.html", context)

    

def board_save(request):
    try:
        username = request.user.username
        title = request.POST["title"]
        detail = request.POST["detail"] 
        board(username=username, title = title, detail=detail, write_date = datetime.now().strftime('%Y%m%d'), enable_yn = 'y').save() 
    except Exception as ex:
       #conn.rollback()
        print(ex.__str__)
    # finally:
    #     print("finish")
    return redirect('board_list')

def board_detail(request, id):
    try:
        boardDetail = board.objects.get(pk=id)       
        
        context = {
            "post" : boardDetail,
        }
        #boardDetail.objects.filter(pk=id).update(hits = boardDetail.hits + 1)
        
        hits = int(boardDetail.hits) + 1
        hits = str(hits)
        boardDetail.hits = hits
        boardDetail.save()
    except Exception as ex:
        print(ex.__str__)

    return render(request, 'board_detail.html', context)

def board_delete(request):
    try:         
        dList = request.POST.getlist('dList[]')
        
        #boardDetail = board.objects.get(pk=id)  
        for id in dList:
            boardDetail = board.objects.get(pk=id)  
            boardDetail.enable_yn = 'n'
            boardDetail.save()
    except Exception as ex:
        print(ex.__str__)

    return redirect('board_list')
    #return render(request, "board_list.html")