from django.urls import path
from board import views


urlpatterns = [  
    path('board/list/', views.board_list, name = 'board_list'),
    path('board/modify/<id>/', views.board_modify, name = 'board_modify'),
    path('board/save/', views.board_save, name = 'board_save'),
    path('board/new/', views.board_new, name = 'board_new'),
    path('board/delete/', views.board_delete, name = 'board_delete'),
    path('board/detail/<id>/', views.board_detail, name = 'board_detail'),
    
]

