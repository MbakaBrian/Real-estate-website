from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm  # Add this import

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            ...
        else:
            # Return an 'invalid login' error message.
            ...
    else:
        return render(request, 'authenticate/login.html', {})

def register_user(request):
    if request.method == "POST":  # Fix capitalization: "POST" instead of "post"
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Registration Successfull"))
            return redirect('home')
        else:
            # Indentation fix and move form initialization outside the if block
            form = UserCreationForm(request.POST)
    else:
        form = UserCreationForm()  # Move this line outside the if block

    return render(request, 'authenticate/register_user.html', {"form": form})  # Move the return statement outside the else block
