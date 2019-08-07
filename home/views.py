from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.


def home_view(request):
    context = {
    }
    if request.user.is_authenticated:
        return HttpResponseRedirect('/board/')
    return render(request,"home.html",context)


def about_view(request):
    context = {

    }
    return render(request,"about/about_me.html",context)
