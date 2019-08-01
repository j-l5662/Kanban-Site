from django.shortcuts import render
from cards.models import Card
# from django.apps import apps
# Create your views here.


def board_home_view(request):
    querySet = Card.objects.all()
    context = {
        "cards" : querySet

    }
    return render(request, "home.html",context)
