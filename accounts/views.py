from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import login, authenticate
from django.core.validators import validate_email
from .forms import UserForm
from board.models import Board
# Create your views here.

def user_register_view(request):
    context = {

    }
    if request.method == 'POST':
        form = UserForm(request.POST or none)
        print(form)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username,password=raw_password)
            # user = User.objects.create_user(**form.cleaned_data)
            login(request,user)
            Board.objects.create(user=user,title=username+" Board")
            return HttpResponseRedirect('/board/')
        else:
            print("Invalid Information")

        return render(request,'registration/registration.html',context)

    return render(request,'registration/registration.html',context)
