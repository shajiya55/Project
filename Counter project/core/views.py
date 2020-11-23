from django.shortcuts import render

# counter.
def home(request):
    ct=request.session.get('count',0)
    newcount=ct+1
    request.session['count']=newcount
    return render(request,'home.html',{'c':newcount})
