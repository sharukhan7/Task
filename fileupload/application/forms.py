from django import forms  
from .models import StudentForm
class StudentFormform(forms.ModelForm):  
    class Meta:
        model = StudentForm
        fields = "__all__"