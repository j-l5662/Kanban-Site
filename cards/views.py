from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Card
from .forms import CardForm
from board.models import Board
# Create your views here.


def add_card_view(request):
    form = CardForm(request.POST or None)
    if form.is_valid():
        print(request.user)
        board = Board.objects.get(user=request.user)
        print(board)
        form.save(board)
        form = CardForm()
        return HttpResponseRedirect('/home/')
    context = {
        "form": form
    }
    return render(request, "cards/add_card.html",context)

def edit_card_details(request,id):
    initial_data = {
        'title': "title",
        'description': "des",
        'stage': "todo"
    }
    obj = Card.objects.get(id=id)
    form = CardForm(request.POST or None,instance=obj)
    if form.is_valid():
        board = Board.objects.get(user=request.user)
        print(board)
        form.save(board)
        form = CardForm()
        return HttpResponseRedirect('/home/')
    context = {
        "form": form
    }
    return render(request, "cards/add_card.html",context)
