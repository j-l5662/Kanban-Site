from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponseNotFound
from .models import Card
from .forms import CardForm
from board.models import Board
# Create your views here.


def add_card_view(request):
    if not request.user.is_authenticated:
        return HttpResponseNotFound('<h1>Page Not Found</h1>')
    form = CardForm(request.POST or None)
    if form.is_valid():
        print(request.user)
        board = Board.objects.get(user=request.user)
        print(board)
        form.save(board)
        form = CardForm()
        return HttpResponseRedirect('/board/')
    context = {
        "form": form
    }
    return render(request, "cards/add_card.html",context)

def edit_card_details(request,id):
    obj = Card.objects.get(id=id)
    form = CardForm(request.POST or None,instance=obj)
    context = {
        "form": form
    }
    if request.POST.get("Save"):
        print('Save')
        if form.is_valid():
            board = Board.objects.get(user=request.user)
            print(board)
            form.save(board)
            form = CardForm()
            return HttpResponseRedirect('/board/')
        else:
            print('invalide')
    elif request.POST.get("Delete"):
        print("Delete1")
        obj = get_object_or_404(Card,id=id)
        if request.method == "POST":
            obj.delete()
        return HttpResponseRedirect('/board/')
    return render(request, "cards/add_card.html",context)
