from django.shortcuts import render

from forms import RegistrationForm
from django.contrib import messages


# Create your views here.


def registration(request):
    if request=='POST':
        fm=RegistrationForm(request.POST)
        if fm.is_valid():
            fm.save()
            message.success(request,'Registration create sucessfully')
    else:
        fm=RegistrationForm()
    return render(request,'registration.html',{'fm':fm})
    
