from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect

from report.models import Report


def logout_request(request):
    logout(request)
    messages.info(request, 'Logged out')
    return redirect('login')


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if user.profile.role == 2 or user.profile.role == 3:
                    return redirect('index')
                elif user.profile.role == 1:
                    return redirect('log_cash')
        else:
            messages.error(request, "Please try again!")
    form = AuthenticationForm()
    return render(request, 'user/login.html', {'form': form, })
