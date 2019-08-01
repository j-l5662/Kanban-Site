from django.urls import path
from .views import add_card_view, edit_card_details

app_name = 'cards'

urlpatterns = [
    path('add/',add_card_view, name='add_card_view'),
    path('<int:id>/edit/',edit_card_details, name ='edit_view'),
]
