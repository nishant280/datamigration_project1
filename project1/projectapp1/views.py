from django.shortcuts import render,HttpResponseRedirect
from .forms import StudentRegistration
from .models import User
from django.contrib import messages
# Create your views here.

# This will be used to add and show the data....
def add_show(request):
    if request.method=='POST':
        fm=StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            adr = fm.cleaned_data['address']
            num = fm.cleaned_data['number']
            gen = fm.cleaned_data['gender']
            reg = User(name=nm,email=em,address=adr,number=num,gender=gen,)
            reg.save()
            fm=StudentRegistration()
            messages.success(request,"The data added Successfully in Table")
    else:
        fm=StudentRegistration()
    stud = User.objects.all()
    return render(request, 'enroll/addandshow.html',{'form':fm,'stu':stud})

# This functio will update/Edit the data...

def update_data(request,id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm=StudentRegistration(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
            messages.success(request,"The Data updated Successfully in Table")
    else:
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(instance=pi)
        
    return render(request, 'enroll/updatestudent.html', {'form':fm})

# This function will be used to Delete the data....

def delete_data(request,id):
    if request.method=='POST':
        pi= User.objects.get(pk=id)
        pi.delete()
        messages.success(request,"The data deleted Successfully from the Table")
        return HttpResponseRedirect('/')