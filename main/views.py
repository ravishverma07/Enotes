from django.shortcuts import render
from .models import Note , Feedback,CustomUser
from django.db.models import Q
from allauth.socialaccount.models import SocialAccount



def home(request):
    feedback = Feedback.objects.order_by('-id')[:6]
    

    if request.user.is_authenticated and request.user.socialaccount_set.filter(provider='google').exists():
        # Get the user's data from the OAuth response
        social_account = SocialAccount.objects.get(user=request.user, provider='google')
        user_data = social_account.extra_data

        # Extract user information
        name = user_data.get('name', '')
        username = user_data.get('username', '')
        email = user_data.get('email', '')
        profile_photo_url = user_data.get('picture', '')
        # print(user_data,"userdata")
        # print(name,"name")
        # print(username,"username")
        # print(email,"email")
        # print(profile_photo_url,"photo")

    
        user_profile, created = CustomUser.objects.get_or_create(
        username=username,
        defaults={
            'name': name,
            'email': email,
            'profile_photo_url': profile_photo_url,
          
        }
    )
        if user_profile.name != name or user_profile.email != email or user_profile.profile_photo_url != profile_photo_url:
           user_profile.name = name
           user_profile.email = email
           user_profile.profile_photo_url = profile_photo_url
           user_profile.save()

    context = {
        
            'feedback':feedback
        }

    return render(request, 'home.html',context)

def notes(request):
    notes = Note.objects.all()
    return render(request,'notes.html', {'notes' : notes})
def cpro(request):
    notes = Note.objects.all()
    return render(request,'c_programming.html', {'notes' : notes})
def office(request):
    notes = Note.objects.all()
    return render(request,'c_programming.html', {'notes' : notes})
def cf(request):
    notes = Note.objects.all()
    return render(request,'c_programming.html', {'notes' : notes})
def eng(request):
    notes = Note.objects.all()
    return render(request,'c_programming.html', {'notes' : notes})
def maths(request):
    notes = Note.objects.all()
    return render(request,'c_programming.html', {'notes' : notes})

def search(request):
    query = request.GET.get('q')
    print(query)
    
    if query:
        notes = Note.objects.filter(
            Q(title__icontains=query) | Q(description__icontains=query)
        )
    else:
        notes = Note.objects.none() 

    return render(request, 'search_result.html', {'notes': notes, 'query': query})

def feedback(request):
    thank = None
    if request.method == 'POST':
        feedback = request.POST['feedback']


        user = request.user 
 
        feedback = Feedback(user=user, text=feedback)
        
        feedback.save()
        
        thank = "Thank You for your Feedback"
        
    return render(request,'feedback.html',{'thank': thank})
