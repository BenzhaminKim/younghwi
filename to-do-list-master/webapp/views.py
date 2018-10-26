from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    return render(request,'webapp/home.html')
    
@login_required
def note(request):
    context = {
        'posts':Post.objects.all()
    }
    return render(request, 'webapp/note.html',context)

def about(request):
    return render(request, 'webapp/about.html')
