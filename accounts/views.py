from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import login, authenticate
from django.core.validators import validate_email
from .forms import UserForm
from board.models import Board
# Create your views here.

def user_register_view(request):
    email = request.POST.get('register')
    print(email)
    if email is None or email is "":
        return HttpResponseRedirect('/')
    try:
        validate_email(email)
    except:
        print("Invalid Email")
        return HttpResponseRedirect('/')
    initial_data = {
        'email': email,
    }
    form = UserForm(initial=initial_data)
    print(initial_data)
    context = {
        'form': form
    }
    print(form)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username,password=raw_password)
            login(request,user)
            Board.objects.create(user=user,title=username+" Board")
            return HttpResponseRedirect('/board/')
        else:
            print("Invalid Information")

        return render(request,'registration/registration.html',context)

    return render(request,'registration/registration.html',context)
