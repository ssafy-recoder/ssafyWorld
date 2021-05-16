from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, login as auth_login
from django.contrib.auth import logout as auth_logout
from django.views.decorators.http import require_http_methods
from .forms import CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def index(request):
    return render(request, 'accounts/index.html')


@require_http_methods(['GET', 'POST'])
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            # form.save()를 하면 현재 가입된 유저가 반환된다...?!
            user = form.save()
            auth_login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('homepage:index', user.pk)
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user(), backend='django.contrib.auth.backends.ModelBackend')
            return redirect('homepage:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)


def logout(request):
    auth_logout(request)
    return redirect('accounts:index')
