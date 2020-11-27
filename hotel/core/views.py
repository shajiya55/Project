from django.shortcuts import render
from .forms import proomforms,Contactform,ReserveForm
from .models import proom,Contact
# Home
def home(request):
    context={'home':'active'}
    return render(request,'index.html',context)

# about
def about(request):
    context={'about':'active'}
    return render(request,'about.html',context)  
    
# room
def room(request):
    if request.method=='POST':
        fm=proomforms(request.POST,request.FILES)
        if fm.is_valid:
            fm.save()
    fm=proomforms()
    stud=proom.objects.all().order_by('price')    
    return render(request,'rooms.html',{'fm':fm,'stud':stud,'room':'active'})    
 
# booknow
def booknow(request):
    if request.method=='POST':
        fm=ReserveForm(request.POST)
        if fm.is_valid:
            fm.save()
            fm=ReserveForm()
    else:
        fm=ReserveForm() 
    return render(request,'booknow.html',{'fm':fm,'booknow':'active'})    

# contact
def contact(request):
    if request.method=='POST':
        fm=Contactform(request.POST)
        if fm.is_valid:
            fm.save()
            fm=Contactform()
    else:
        fm=Contactform()        
    return render(request,'contact.html',{'fm':fm,'contact':'active'})    

  