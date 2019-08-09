from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import login, authenticate
from .forms import UserForm
from board.models import Board
# Create your views here.

def user_register_view(request):
    email = request.POST.get('register')
    initial_data = {
        'username': "",
        'email': email,
        'password1': "",
        'password2': "",
    }
    print(email)
    form = UserForm(request.POST or None,initial=initial_data)
    context = {
        'form': form
    }
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
