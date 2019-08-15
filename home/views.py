from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.validators import validate_email
# Create your views here.


def home_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/board/')

    if request.method == "POST":
        print("YES")
        email = request.POST.get('register')
        print(email)
        if email is None or email is "":
            return HttpResponseRedirect('/')
        try:
            validate_email(email)
            context = {
                'email': email,
            }
            return render(request,'registration/registration.html',context)
        except:
            print("Invalid Email")
            return HttpResponseRedirect('/')

    return render(request,"home.html")


def about_view(request):
    context = {

    }
    return render(request,"about/about_me.html",context)
