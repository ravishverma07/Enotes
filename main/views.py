from django.shortcuts import render
from .models import Note , Feedback
from django.db.models import Q


def home(request):
    feedback = Feedback.objects.all()
    return render(request, 'home.html',{'feedback':feedback})

def notes(request):
    notes = Note.objects.all()
    return render(request,'notes.html', {'notes' : notes})
def cpro(request):
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
        notes = Note.objects.none()  # Return an empty queryset if no query is provided
    
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

