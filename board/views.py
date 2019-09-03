from django.shortcuts import render, render_to_response
import sqlite3
import json
import openpyxl
import os
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils import timezone
from django.db import transaction
from datetime import datetime
import logging
from django.contrib.auth.models import Permission, User
from django.shortcuts import get_object_or_404
from board.models import board


logger = logging.getLogger(__name__)

def board_list(request):
    try:
        context = {

        }
    finally:
        print("finish")
    return render(request, "board_list.html", context)

def board_write(request):
    try:
        context = {

        }
    finally:
        print("finish")
    return render(request, "board_write.html", context)

def board_save(request):
    try:
        username = request.User.username
        title = request.GET["title"]
        detail = request.GET["detail"]
        hits = 0
        recommend = request.GET["recommend"]
        board(username=username, title = title, detail=detail, hits=hits, recommend=recommend).save()
        context = [
            
        ]
    finally:
        print("finish")
    return render(request, "board_write.html", context)