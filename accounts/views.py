from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib import messages, auth

# Create your views here.

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        if '@' and '.com' not in email:
                messages.error(request, 'Email not correct')
        else:
            ls = email.split('@')
            username = ls[0]
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Invalid credentials')
                return redirect('login')



    return render(request, "accounts/login.html")



def register(request):
    if request.method == 'POST':
        email = request.POST['email'],
        password = request.POST['password'],
        confirm_password = request.POST['confirm_password']

        
        my_str = ', '.join(map(str, password))
        password = my_str
        my_str = ', '.join(map(str, email))
        email = my_str
        ls = my_str.split('@')
        username = ls[0]
        if '@' and '.com' not in email:
            messages.error(request, 'Email not correct')
            return redirect('register')
        if len(password)<8:
            messages.error(request, 'Password length too short')
            return redirect('register')
             

        if password == confirm_password:
            check = User.objects.filter(email = email).exists()
            print(check)
            if User.objects.filter(email = email).exists():
                messages.error(request, 'Email already registered')
                print('no email')
            else:
                user = User.objects.create_user(username = username, email=email,password=password)
                user.save()
                messages.success(request, "Account created successfully")
                print('created')
                return redirect('login')
            
        else:
            messages.error(request,'Password do not match!')
            return redirect('register')
        
    
    return render(request,'accounts/register.html')

def logout_user(request):
    logout(request)
    return redirect('home')

# def dashboard(request):
#     return render(request, 'accounts/dashboard.html')