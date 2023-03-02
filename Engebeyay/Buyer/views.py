from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def home(request):

    return render(request, 'index.html')


def signin(request):

    return render(request, "signin.html")
