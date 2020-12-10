from django.shortcuts import render,HttpResponse
from .models import limit,market,stop
from.forms import limitform,marketform,stopform
# Create your views here.
def limitv(request):
    if request.method=='POST':
        fm=limitform(request.POST)
        if fm.is_valid():
            fm.save()
    else:
        fm=limitform()
    return render(request,'base.html',{'fm':fm})            

def marketv(request):
    if request.method=='POST':
        fmo=marketform(request.POST)
        if fmo.is_valid():
            fmo.save()
    else:
        fmo=marketform()
    return render(request,'base.html',{'fm':fmo})   


def stopv(request):
    if request.method=='POST':
        fom=stopform(request.POST)
        if fom.is_valid():
            fom.save()
    else:
        return HttpResponse('not available')
    return render(request,'base.html',{'fm':fom})       
