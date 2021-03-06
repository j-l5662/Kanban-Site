from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.validators import validate_email
from accounts.forms import UserForm
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
            initial_data = {
                'email': email,
            }
            form = UserForm(initial=initial_data)
            context = {
                'form': form,
            }
            return render(request,'registration/registration.html',context)
        except:
            print("Invalid Email")
            return HttpResponseRedirect('/')

    return render(request,"home.html")


def about_view(request):
    text = "Johann Lau is a computer science masters student at Georgia Tech that is willing to learn and grow as a software developer. His experience with software design and testing, solution architect, and cybersecurity provides an holistic and technical approach to problem solving."
    context = {
        "about_me" : text,
    }
    return render(request,"about/about_me.html",context)
