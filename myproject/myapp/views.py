from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from . forms import StudentForm
from . models import Student

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

def viewStudent(request):
    allstd=Student.objects.all()
    context={'allstd':allstd}
    return render(request, 'view_student.html', context)

def delStudent(request):
    id=request.POST.get('id')
    std=Student.objects.get(id=id)
    std.delete()
    return redirect('view-std')
