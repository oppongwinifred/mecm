from django import forms
from django.db.models import fields
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


from .models import *

class Add_Student_Form(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'  

class Student_Daily_Pay_Form(forms.ModelForm):
    class Meta:
        model = Payment
        fields = '__all__'    

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username','email','password1','password2']                    
                  