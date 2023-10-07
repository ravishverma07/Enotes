from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.db import IntegrityError
from .models import CustomUser
from django.contrib import auth
from allauth.socialaccount.models import SocialAccount



# def signup(request):

#     if request.method == 'POST':
#             username = request.POST.get('Username').strip()
#             password = request.POST.get('Password').strip()
#             confirmpass = request.POST.get('ConfirmPassword').strip()
#             gender = request.POST.get('gender')

#             if password != confirmpass:
#                 error_message = "Passwords do not match"
#                 return render(request, 'signup.html', {'error_message': error_message})

#             try:
#                 email = user.email
#                 user = CustomUser.objects.create_user(
#                     username=username,
#                     password=password,
#                     gender=gender ,
#                     email=email
#                 )
#                 login(request, user)
#                 return redirect('../',)
#             except IntegrityError:
#                 already_exist = "Username is not available. Try a different username."
#                 return render(request, 'signup.html', {'already_exist': already_exist})

#     return render(request, 'signup.html')
def google_auth_callback(request):
    # if request.user.is_authenticated and request.user.socialaccount_set.filter(provider='google').exists():

    #     social_account = SocialAccount.objects.get(user=request.user, provider='google')
    #     user_data = social_account.extra_data

    return redirect('/')


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
    return redirect('logapi')
def user_profile(request):
    
    return render(request,'profile.html')
def logapi(request):
    
    return render(request, 'logapi.html',)
   
