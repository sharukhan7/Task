from django.shortcuts import render
from django.contrib import messages
# Create your views here.

from django.shortcuts import render  
from application.form import StuForm  
  
def index(request):  
    
    if request.method == 'POST' :
        stu = StuForm(request.POST) 
        if stu.is_valid():
            stu.save()
            messages.success(request,'Registration create sucessfully') 
    else:
        stu = StuForm()
    return render(request,"index.html",{'form':stu})