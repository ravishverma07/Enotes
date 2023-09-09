from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.db import IntegrityError
from .models import CustomUser
from django.contrib import auth

def signup(request):
    if request.method == 'POST':
        email = request.POST.get('email').strip()
        username = request.POST.get('Username').strip()
        password = request.POST.get('Password').strip()
        confirmpass = request.POST.get('ConfirmPassword').strip()
        gender = request.POST.get('gender')

        if password != confirmpass:
            error_message = "Passwords do not match"
            return render(request, 'signup.html', {'error_message': error_message})

        try:
            user = CustomUser.objects.create_user(
                username=username,
                password=password,
                email=email,
                gender=gender  # Set the gender field
            )
            login(request, user)
            return redirect('../')
        except IntegrityError:
            already_exist = "Username is not available. Try a different username."
            return render(request, 'signup.html', {'already_exist': already_exist})

    return render(request, 'signup.html')

# Other views remain unchanged


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        try:
            user = CustomUser.objects.get(username=username)

            print("Password:", password)
            user = auth.authenticate(username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('../')
            else:
                error_login = "Incorrect credentials"
                return render(request, 'login.html', {'error_login': error_login})
        
        except CustomUser.DoesNotExist: 
            doesnot_exist = "User doesn't exist"
            return render(request, 'login.html', {'doesnot_exist': doesnot_exist})
    
    return render(request, 'login.html')
def user_logout(request):
    logout(request)
    return redirect('login')
def user_profile(request):
    
    return render(request,'profile.html')
# def verification(request):
#     #  email = request.session.get('email')
#      return render(request,'verification.html', {'email': email})
   
