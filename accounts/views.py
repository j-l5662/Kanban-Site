from django.shortcuts import render

# Create your views here.

def user_register_view(request):
    context = {

    }
    return render(request,'registration/registration.html',context)
