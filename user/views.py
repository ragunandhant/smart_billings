from django.shortcuts import render,redirect

# Create your views here.
from .forms  import SignUpForm,LoginForm
from django.contrib.auth.models import User


from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required

from .models import userProfile
from .forms import UserProfileForm

@login_required
def register_request(request):
    if request.method=="POST":
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:index')
    else:
            form=SignUpForm()
    return render(request,'register.html',{'form': form})
      


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome back, {username}!")
                if user.is_staff:
                    return redirect()
                return redirect('core:index')  # Replace 'home' with your desired URL
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})
def logout(request):
    if request.user.is_authenticated:
        username = request.user.username
        auth_logout(request)
        messages.success(request, f"Goodbye, {username}! You have been logged out.")
    return redirect('core:index')