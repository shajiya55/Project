from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def cont(request):
    context={'cont':'active'}
    return render(request,'cont.html',context)