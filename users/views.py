from email import message
import re
from django.shortcuts import redirect, render
from .models import Profile
#from aoc.models import Question
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
from .forms import ProfileForm
from django.views import View

# Create your views here.

def loginUser(request):
    page = 'login'
    
    if request.method == 'POST':
        username = request.POST['username'].lower()
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            

            return redirect(request.GET['next'] if 'next' in request.GET else 'users:account')
        else:
            messages.error(request, "Username or Password doesn't match")
           
    context = {'page': page}
    return render(request, 'users/login_register.html', context)


def logoutUser(request):
    logout(request)
    messages.info(request, 'User successfully logged out!')
    return redirect('users:login')


def registerUser(request):
    page = 'register'
    form = CustomUserCreationForm()
    context = {'page': page,
               'form': form
               }

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            user=form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'User created successfully')
            login(request, user)
            return redirect('users:profiles-all')
        else:
            messages.error(
                request, 'Some error occurred during registration')
            print(form.errors)
    

    context={'page':page, 'form':form, }      
    return render(request, 'users/login_register.html', context)


