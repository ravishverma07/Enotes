from .models import CustomUser

def google_user_data(request):
    google_user = None

    if request.user.is_authenticated and request.user.socialaccount_set.filter(provider='google').exists():
        try:
            google_user = CustomUser.objects.get(username=request.user.username)
            print(google_user.name)
            print(google_user.username)
            print(google_user.email)
            print(google_user.profile_photo_url)
        except CustomUser.DoesNotExist:
            google_user = None 
  
    return {'google_user': google_user}
