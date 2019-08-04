from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from cards.models import Card
import itertools
# from django.apps import apps
# Create your views here.


def board_view(request):
    if request.user.is_authenticated:
        todoItems = Card.objects.filter(stage='todo')
        inprogItems = Card.objects.filter(stage='inpr')
        doneItems = Card.objects.filter(stage='done')

        queryItems = list(itertools.zip_longest(todoItems,inprogItems,doneItems))

        context = {
            "zipCards" : queryItems

        }
        return render(request, "board/board_detail.html",context)
    else:
        return HttpResponseNotFound('<h1>Page not found</h1>')

def board_list_view(request):
    context = {
    }
    return render(request,"board/board_list.html",context)
