from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from . forms import StudentForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return HttpResponse('<h1>About Page</h1>')

def contact(request):
    return render(request, 'contact.html')

def add_student(request):
    if request.POST:
       stdform=StudentForm(request.POST)
       stdform.save()
    else:
        stdform=StudentForm()
    context={'form':stdform}
    return render(request, 'add_student.html', context)
