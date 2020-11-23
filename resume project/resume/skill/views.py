from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def skill(request):
    context={'skill':'active'}
    return render(request,'skill.html',context)
