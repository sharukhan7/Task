from django.shortcuts import render
from .forms import EmployeeForm

# Create your views here.

def emp(request):  
    if request.method == "POST":  
        form = EmployeeForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()
                return redirect('/')  
            except:  
                pass  
    else:  
        form = EmployeeForm()  
    return render(request,'index.html',{'form':form})  