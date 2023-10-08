from django.shortcuts import render ,redirect
from .models import Note , Feedback
from django.db.models import Q



def home(request):

    feedback = Feedback.objects.order_by('-id')[:6]
     
    context = {
        
            'feedback':feedback
        }

    return render(request, 'home.html',context)

def notes(request):

    notes = Note.objects.all()
    return render(request,'notes.html', {'notes' : notes})

def cpro(request):

    notes = Note.objects.filter(subject="C Programming")
    return render(request,'c_programming.html', {'notes' : notes})

def office(request):

    notes = Note.objects.filter(subject="Office Automation Tools")
    return render(request,'office.html', {'notes' : notes})


def cf(request):

    notes = Note.objects.filter(subject="Computer Fundamentals")
    return render(request,'cf.html', {'notes' : notes})

def eng(request):

    notes = Note.objects.filter(subject="English")
    return render(request,'eng.html', {'notes' : notes})

def maths(request):

    notes = Note.objects.filter(subject="Maths")
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

       
 
        note = Note(title=title,
                    description=description,
                    subject=subject,
                    pdf_file=pdf_file,
                    user=user)
        
        note.save()
        
        thank = f"Thank You {user} for Contributing"

    return render(request,"upload_notes.html",{'thank': thank})