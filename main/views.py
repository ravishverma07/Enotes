from django.shortcuts import render ,redirect
from .models import Note , Feedback, Skill ,CustomUser
from django.db.models import Q
from django.core.paginator import Paginator
from allauth.socialaccount.models import SocialAccount


def paginate_notes(request, notes):
    page = request.GET.get('page')
    paginator = Paginator(notes, 15) 
    page_notes = paginator.get_page(page)
    return page_notes


def google_data(request):
  
    if request.user.is_authenticated and request.user.socialaccount_set.filter(provider='google').exists():
    
            social_account = SocialAccount.objects.get(user=request.user, provider='google')
            user_data = social_account.extra_data

            name = user_data.get('name', '')
            given_name = user_data.get('given_name', '')
            email = user_data.get('email', '')
            profile_photo_url = user_data.get('picture', '')

            custom_user, created = CustomUser.objects.get_or_create(email=email)
            custom_user.name = name
            custom_user.email = email
            custom_user.profile_photo_url = profile_photo_url
            custom_user.save()


           
            if created==True:
                # Redirect to a page for new users
                return redirect('notes')
            else:
           
                return redirect('about')
    else:
        return redirect('/')       
 

def home(request):
    skills =  Skill.objects.all()
    feedback = Feedback.objects.order_by('-id')[:6]
     
    context = {
        
            'feedback':feedback,
            'skills':skills
        }

    return render(request, 'home.html',context)

def notes(request):

    note = Note.objects.order_by('-id')
    notes = paginate_notes(request, note)
    return render(request,'notes.html', {'notes' : notes})

def cpro(request):

    notes = Note.objects.filter(subject="C Programming").order_by('id')
    # note = paginate_notes(request, note)
    return render(request,'c_programming.html', {'notes' : notes})

def office(request):

    notes = Note.objects.filter(subject="Office Automation Tools")
    # note = paginate_notes(request, note)
    return render(request,'office.html', {'notes' : notes})


def cf(request):

    notes = Note.objects.filter(subject="Computer Fundamentals")
    # note = paginate_notes(request, note) 
    return render(request,'cf.html', {'notes' : notes})

def eng(request):

    notes = Note.objects.filter(subject="English")
    # note = paginate_notes(request, note)
    return render(request,'eng.html', {'notes' : notes})

def maths(request):

    notes = Note.objects.filter(subject="Maths")
    # note = paginate_notes(request, note)
    return render(request,'maths.html', {'notes' : notes})

def about(request):
    return render(request,"about.html")


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

    thank = ''
    if request.method == 'POST':
        feedback = request.POST['feedback']


        user = request.user 
 
        feedback = Feedback(user=user, text=feedback)
        
        feedback.save()
        
        thank = "Thank You for your Feedback"
         
    return render(request,'feedback.html',{'thank': thank})

def upload_notes(request):
    thank = ''
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        subject = request.POST['subject']
        pdf_file = request.FILES['pdf_file']
        user = request.user
        
        max_size = 300 * 1024  # 300KB
        if pdf_file.size > max_size:
                error_message = "file should be less than 300kb"
                return render(request, 'upload_notes.html', {'error_message': error_message})
       
 
        note = Note(title=title,
                    description=description,
                    subject=subject,
                    pdf_file=pdf_file,
                    user=user)
        
        note.save()
        
        thank = f"Thank You {user} for Contributing"

    return render(request,"upload_notes.html",{'thank': thank})