from django.shortcuts import render
from django.http import HttpResponseRedirect
from.models import Student
from.forms import Studentinfo


# For creating data.
def add(request):
    if request.method=='POST':
        fm=Studentinfo(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            pw=fm.cleaned_data['password']
            em=fm.cleaned_data['email']
            reg=Student(name=nm,email=em,password=pw)
            reg.save()
            fm=Studentinfo()   
    else:
        fm=Studentinfo() 
    stud=Student.objects.all()           
    return render(request,'add.html',{'form':fm,'st':stud})

# For updating data.
def update(request,id):
    if request.method=='POST':
        pi=Student.objects.get(pk=id)
        fm=Studentinfo(request.POST,instance=pi) 
        if fm.is_valid():
            fm.save()
    else:
        pi=Student.objects.get(pk=id)
        fm=Studentinfo(instance=pi)  
    context={'form':fm}
    return render(request,'show.html',context)            

# For deleting data.
def delete(request,id):
    if request.method=='POST':
        pi=Student.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')