from django.urls import path
from exam import views

urlpatterns = [
    path('', views.getExample),
    path('get_title_content/', views.getTitleContent)
]