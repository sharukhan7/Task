from django.shortcuts import render

from .forms import RegistrationForm
from django.contrib import messages

# Create your views here.

def registration(request):
    print(request)
    if request.method == 'POST' :
        print('in')
        fm=RegistrationForm(request.POST)
        if fm.is_valid():
            print('is valid')
            fm.save()
            messages.success(request,'Registration create sucessfully')
    else:
        print('out')
        fm=RegistrationForm()
    return render(request,'registration.html',{'fm':fm})