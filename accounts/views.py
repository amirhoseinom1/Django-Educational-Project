from django.shortcuts import render,redirect
from .forms import UserCreateForm,UserLoginForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout


def create_user(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.create_user(cd['username'], cd['email'], cd['password'])
            user.first_name = cd['firstname']
            user.last_name = cd['lastname']
            user.save()
            messages.success(request, 'user created successfully','success')
            return redirect("home")
    else:
        form = UserCreateForm()
        return render(request, 'user_create.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'logged in succesfully','success')
                return redirect("home")
            else:
                messages.error(request, 'username or password is wrong','danger')
                return render(request, 'user_login.html', {'form': form})
    else:
        form = UserLoginForm()
        return render(request, 'user_login.html', {'form':form})


def logout_user(request):
    logout(request)
    messages.success(request, 'logged out successfully','success')
    return redirect("home")






