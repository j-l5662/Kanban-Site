from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import login, authenticate
from django.core.validators import validate_email
from .forms import UserForm
from board.models import Board
# Create your views here.

def user_register_view(request):
    email = ""
    initial_data = {
        'email': email,
    }
    form = UserForm(initial=initial_data)
    print(request.POST)
    context = {
        'form': form
    }
    if request.method == 'POST':
        print("POST")
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username,password=raw_password)
            user = User.objects.create_user(**form.cleaned_data)
            login(request,user)
            print("Authenticated")
            Board.objects.create(user=user,title=username+" Board")
            return HttpResponseRedirect('/board/')
        else:
            print(form)
            print("Invalid Information")

        return render(request,'registration/registration.html',context)

    return render(request,'registration/registration.html',context)
