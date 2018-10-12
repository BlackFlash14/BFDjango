from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


def registration(request):
    form = UserCreationForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('todos')
    return render(request, 'registration.html', {'form': form})


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None and  user.is_active:
            auth.login(request, user)
            return redirect('todos')
        else:
            error="What's wrong with u?"
            return redirect('login.html', {'error': error})
    else:
        return render(request, 'login.html')

