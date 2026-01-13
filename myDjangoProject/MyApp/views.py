from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Features
from django.contrib.auth.models import User, auth 
from django.contrib import messages

# Create your views here.
def index(request):
    feature = Features.objects.all()
    # context = {
    #     'name' : 'John Wick',
    #     'Weapon' : 'Guns, lots of guns..!',
    #     'age' : 45,
    # }
    return render(request, 'index.html' ,{'feature': feature})

def countWord(request):
    words = request.POST['words']
    count_of_words = len(words.split())
    return render(request, 'countWord.html', {'amount' : count_of_words})


def register(request):
    if request.method == 'POST': 
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password'] 
        passwordRep = request.POST['passwordRep']

        if password == passwordRep:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Already Registered')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Already Used')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save();
                return redirect('login')
        else:
            messages.info(request, 'Password Must Be Equal')
            return redirect('register')
        
    else:
        return render(request, 'register.html')
    
def login_view(request):
    return render(request, 'login.html')
