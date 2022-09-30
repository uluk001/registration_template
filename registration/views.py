from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout

# Create your views here.
def base(request):
    return render(request, 'base.html') 

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('base')

    else:
        form = UserCreationForm()

    return render(request, 'user.html', {'form':form})    
        

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('base')
    else:
        form = AuthenticationForm()

    return render(request, 'user.html', {'form':form})



def signout(request):
    logout(request)
    return render(request, 'base.html')