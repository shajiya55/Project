from django.shortcuts import render
from.models import image
from.forms import imageForm
# Create your views here.
def home(request):
    if request.method=='POST':
        fm=imageForm(request.POST,request.FILES)
        if fm.is_valid:
            fm.save()
    fm=imageForm()
    stud=image.objects.all()
    return render(request,'home.html',{'stud':stud,'fm':fm})    
        
