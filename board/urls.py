from django.urls import path
from .views import board_home_view

app_name = 'board'

urlpatterns = [
    path('',board_home_view, name ='board'),
]
