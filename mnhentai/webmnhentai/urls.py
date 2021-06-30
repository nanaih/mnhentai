from django.urls import path

from . import views

app_name = 'nhentai'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:doujin_id>/', views.details, name='details'),
    path('<int:doujin_id>/<int:page_number>/', views.reader, name='reader'),
    path('execute/', views.command, name='exec'),
    path('initialize/', views.init, name='init'),
    path('initdb/', views.init_db, name='initdb'),
    path('search/', views.search, name='search'),
]
