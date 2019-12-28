from django.shortcuts import render
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from apps.accounts.forms import FavoriteStationForm, SignupForm
from apps.accounts.models import FavoriteStation
from django.contrib.auth.models import User
from apps.core import bart

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('home_logged_in')
    else:
        form = AuthenticationForm()

    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)


def sign_up(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()

            # Log-in the user right away
            messages.success(request, 'Account created successfully. Welcome!')
            login(request, user)
            return redirect('home_logged_in')
    else:
        form = SignupForm()

    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)


def logout_view(request):
    logout(request)
    messages.success(request, 'Logged out.')
    return redirect('home_logged_out') 

def remove_favorite(request, station_abbr): 
    station = FavoriteStation.objects.filter(
        user_id=request.user.id,
        station=station_abbr, 
        )
    station.delete()

    # Redirect to wherever they came from
    return redirect(request.META.get('HTTP_REFERER', '/'))

def add_favorite(request, station_abbr): 
    if not FavoriteStation.objects.filter(
        user_id=request.user,
        station=station_abbr, 
    ):
        FavoriteStation.objects.create(
            user=request.user, 
            station=station_abbr
        )

    # Redirect to wherever they came from
    return redirect(request.META.get('HTTP_REFERER', '/'))