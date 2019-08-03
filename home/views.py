from django.shortcuts import render

# Create your views here.


def home_view(request):

    context = {
        "obj": "home"
    }
    return render(request,"home.html",context)
