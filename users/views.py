from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from carts.models import Cart
from users.forms import UserLoginForm, UserRegistrationForm, UserChangesForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)

            if user:
                login(request, user)
                return HttpResponseRedirect(reverse('main:home'))
    else:
        form = UserLoginForm()

    context = {
        'form': form,
    }
    return render(request, "users/login.html", context)


def user_register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = form.instance
            login(request, user)
            if request.POST.get('next', None):
                return HttpResponseRedirect(request.POST.get('next'))

            return HttpResponseRedirect(reverse('main:home'))
    else:
        form = UserRegistrationForm()
    context = {
        'form': form,
    }
    return render(request, "users/registration.html", context)


@login_required
def user_profile(request):
    if request.method == 'POST':
        form = UserChangesForm(data=request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('user:profile'))
    else:
        form = UserChangesForm(instance=request.user)
    context = {
        'form': form,
    }
    return render(request, "users/profile.html", context)


def user_cart(request):
    return render(request, 'users/user_cart.html')
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('main:home'))
