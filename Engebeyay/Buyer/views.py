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
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            fname = user.first_name
            # messages.success(request, "Logged In Sucessfully!!")
            return render(request, "index.html", {"fname": fname})
        else:
            messages.error(request, "Bad Credentials!!")
            return redirect('home')

    return render(request, "signin.html")


def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!!")
    return redirect('home')


def signup(request):
    return render(request, "signup.html")
