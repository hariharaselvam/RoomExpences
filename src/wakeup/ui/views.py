from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

# Create your views here.

@login_required
def index(request):
    return render(request, 'index.html', {})

def signin(request):
    next = request.GET.get('next')
    if next is None and request.POST.get('next') is not None:
        next = request.POST.get('next')

    if next is None:
        next = "/"


    if request.method == "POST":

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            return render(request, 'login.html', {'error': 'fail', 'next': next})

    else:
        return render(request, 'login.html', {'next': next})

@login_required
def signout(request):
    logout(request)
    return render(request, 'logout.html', {'error': ''})
