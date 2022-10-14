from django.shortcuts import render, redirect
from .models import reg,login
from django.contrib import messages
from django.contrib.auth import login, logout


#  Create your views here.


def index(request):
    if request.method == "POST":
        name = request.POST.get("a")
        luid = request.POST.get("b")
        passw = request.POST.get("c")
        print(name)
        print(luid)
        print(passw)
        print(name)
        print(luid)
        print(passw)
        new_log = login(username=luid,password=passw)
        new_log.save()
        new_reg = reg(name=name,username=luid)
        new_reg.save()
    return render(request, "register.html")


# from django.shortcuts import render

# Create your views here.
