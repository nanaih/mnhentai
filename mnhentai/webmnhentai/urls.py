from django.urls import path

from . import views

app_name = 'nhentai'
urlpatterns = [
    path('', views.index, name='index'),
    path('execute/', views.command, name='exec'),
    path('initialize/', views.init, name='init'),
    path('initdb/', views.init_db, name='initdb'),
]
