from django.shortcuts import render
from cards.models import Card
import itertools
# from django.apps import apps
# Create your views here.


def board_view(request):
    todoItems = Card.objects.filter(stage='todo')
    inprogItems = Card.objects.filter(stage='inpr')
    doneItems = Card.objects.filter(stage='done')

    queryItems = list(itertools.zip_longest(todoItems,inprogItems,doneItems))

    context = {
        "zipCards" : queryItems

    }
    return render(request, "board/board_detail.html",context)
