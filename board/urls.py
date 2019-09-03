from django.urls import path
from board import views

urlpatterns = [  
    path('board/list/', views.board_list, name = 'board_list'),
    path('board/write/', views.board_write, name = 'board_write'),
    path('board/save/', views.board_save, name = 'board_save'),

]
