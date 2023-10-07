from allauth.socialaccount.models import SocialAccount

def google_user_data(request):
    google_user = None
    if request.user.is_authenticated and request.user.socialaccount_set.filter(provider='google').exists():
        
        try:
            social_account = SocialAccount.objects.get(user=request.user, provider='google')
            user_data = social_account.extra_data

            name = user_data.get('name', '')
            given_name = user_data.get('given_name', '')
            email = user_data.get('email', '')
            profile_photo_url = user_data.get('picture', '')

            google_user = {'name': name,
                           'given_name': given_name,
                           'email': email,
                           'profile_photo_url': profile_photo_url,
                           }
        except SocialAccount.DoesNotExist:
            # Handle the case when the user does not have a SocialAccount
            print("User does not have a SocialAccount")
    return {'google_user': google_user}



def static_images(request):

    images = {
        'plus': '/static/images/plus.png',
        'myprofile': '/static/images/myprofile.png',
        'logout': '/static/images/logout.png',
    }

    return {'images': images}