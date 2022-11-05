from django.shortcuts import render,redirect
# from .models import
from django.contrib import messages
from django.contrib.auth import login,logout


# Create your views here.

def index(request):
    # request.session['email'] = 'null'
    # request.session['password'] = 'null'
    return render (request,"index_2.html")
