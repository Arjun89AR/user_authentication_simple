from django.shortcuts import render, redirect
from . forms import RegisterForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.decorators.cache import never_cache





# Create your views here.
@never_cache
def register(request):
    if request.user.is_authenticated:
        return redirect("home")
    
    if request.method=='POST':
        form = RegisterForm(request.POST)
        
        if form.is_valid():
            user=form.save()
            login(request, user)
            messages.success(request, "Account created successfully")
            return redirect("login")
            
        else:
            messages.error(request, "Registration Unsuccessful")
    else:
            form = RegisterForm()
    
    return render(request, "register.html", {'form':form})

@never_cache
def login_view(request):
    if request.user.is_authenticated:
        return redirect("home")
        
    if request.method=="POST":
        print("getting in")
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            print("validation")
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(username=username, password=password)
            print("validation complete")
            if user is not None:
                print("user is not none")
                login(request, user)
                messages.info(request, f"You are logged in successfully {username}. ")
                return redirect("home")
            else:
                messages.error(request, "Invalid username or password!!")
        else:
            messages.error(request, "Invalid username or password")
    else:
        form = AuthenticationForm()
    print("getting back to login")
    return render(request, "login.html", {"login_form": form})

@login_required
def logout_view(request):
    logout(request)
    messages.info(request, "You are successfully logged out.")
    return redirect("login")

@login_required
@never_cache
def home(request):
    return render(request, "home.html")


