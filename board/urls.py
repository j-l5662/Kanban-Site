from django.urls import path
from .views import board_view,board_list_view

app_name = 'board'

urlpatterns = [
    path('',board_view, name ='board_view'),
    path('board_list/',board_list_view,name='board_list_view')
]
