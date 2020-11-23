from django.shortcuts import render,HttpResponse
from.models import contact,menu,himg
from.forms import contactForm,menuform,tableform,himgform
# home
def home(request):
    if request.method=='POST':
        fm=himgform(request.POST,request.FILES)
        if fm.is_valid:
            fm.save()
    else:
        fm=himgform()        
    stud=himg.objects.all()
    return render(request,'home.html',{'stud':stud,'fm':fm}) 

# menu
def menuu(request): 
    if request.method=='POST':
        fm=menuform(request.POST,request.FILES)
        if fm.is_valid:
            fm.save()
    else:
        fm=menuform()        
    stud=menu.objects.all().order_by('mprice').reverse() 
    return render(request,'menu.html',{'stud':stud,'fm':fm}) 

# about
def about(request):
    return render(request,'about.html')

# contact
def contact(request):
    if request.method=='POST':
        fm=contactForm(request.POST)
        if fm.is_valid():
            fm.save()
            fm=contactForm()   
    else:
        fm=contactForm()
    return render(request,'contact.html',{'fm':fm})

# table
def table(request):
    if request.method=='POST':
        fm=tableform(request.POST)
        if fm.is_valid:
            fm.save()
            fm=tableform()
    else:
        fm=tableform()
    return render(request,'table.html',{'fm':fm})   


