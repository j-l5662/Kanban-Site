from django.urls import path
from .views import board_view

app_name = 'board'

urlpatterns = [
    path('',board_view, name ='board_view'),
]
