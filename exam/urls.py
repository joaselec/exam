from django.urls import path
from exam import views

urlpatterns = [
    path('', views.getExample),
    path('get_title_content/', views.getTitleContent),
    path('sendResult/', views.sendResult),
    path('statics/', views.statics, name = 'statics'),
    path('statics_false/', views.statics_false),
    path('chart_rate/', views.chart_rate),
    path('data/', views.data),
    
    path('download/', views.download, name = 'download'),
    
]
