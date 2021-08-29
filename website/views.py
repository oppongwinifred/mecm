from django.shortcuts import redirect, render
from django.db.models import Sum
from .models import Student,Payment
from .forms import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .decorators import unauthenticated_user,allowed_users,admin_only
from django.contrib.auth.models import Group

# Create your views here.


'''@unauthenticated_user
def register_view(request):  
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name='students')
            user.groups.add(group)
            messages.success(request, 'Account was created for ' + username)
            return redirect('login')
    context={'form':form}       

    return render(request, 'register.html', context)

@unauthenticated_user
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username OR password is incorrect')    

    context={}
    return render(request, 'login.html', context) 

def logout_view(request):
    logout(request)
    return redirect('login')'''

#@login_required(login_url='login')
#@admin_only
def home_view(request):
    student_created = Student.objects.all()
    all_payment = Payment.objects.all()
    context = {
        'student_created':student_created,
    }
    return render(request, 'index.html', context)

def userPage(request):
    context = {}
    return render(request, 'user.html', context)
    

#@login_required(login_url='login')
#@allowed_users(allowed_roles=['admin'])
def adding_student_view(request):
    form = Add_Student_Form()

    if request.method == "POST":
        form = Add_Student_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    
    context = {
        'form':form,
    }
    return render(request, 'addingstudent.html', context) 

#@login_required(login_url='login')
#@allowed_users(allowed_roles=['admin'])
def updating_student_view(request, pk):
    student1 = Student.objects.get(id=pk)
    form = Add_Student_Form(instance=student1)
    if request.method == "POST":
        form = Add_Student_Form(request.POST,instance=student1)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {
        'form':form,
    }
    return render(request, 'addingstudent.html', context)

#@login_required(login_url='login')
#@allowed_users(allowed_roles=['admin'])
def deleting_student_view(request, pk):
    student1 = Student.objects.get(id=pk)
    context = {'student_name':student1,}
    if request.method == "POST":
        student1.delete()
        return redirect('/')
    return render(request, 'delete.html', context)

#@login_required(login_url='login')
#@allowed_users(allowed_roles=['admin'])
def student_payment_view(request, pk):
    high_price = 80
    low_price = 20
    student = Student.objects.get(id=pk)
    student_payment = student.payment_set.all()
    form = Student_Daily_Pay_Form(initial={'student':student})
    
    if request.method == "POST":
        form = Student_Daily_Pay_Form(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')   
    context = {'student':student,
    'form':form, 
    'student_payment':student_payment, 
    'high_price':high_price,
    'low_price':low_price,}
    return render(request, 'payment.html', context)

#@login_required(login_url='login')
#@allowed_users(allowed_roles=['admin'])
def histories_view(request):
    histowy = Payment.objects.all()
    context = {'histowy':histowy,}
    return render(request, 'history.html', context)


#@login_required(login_url='login')
#@allowed_users(allowed_roles=['admin'])
def records_view(request):
    daily_money_record = Payment.objects.filter().values('when_made').order_by('when_made').annotate(sum=Sum('make_payment'))
    context = {'daily_money_record':daily_money_record}
    return render(request, 'records.html', context)


