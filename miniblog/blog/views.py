from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from.models import blog,loginform
from.forms import contactform,signupform,blogform
from django.contrib.auth import login,logout,authenticate,update_session_auth_hash
from django.contrib.auth.models import User,Group
from django.contrib import messages


# Home.
def home(request):
    context={'home':'active'}
    if request.user.is_authenticated:
            if request.method=='POST':
                fm=blog(request.POST)
                if fm.is_valid():
                    fm.save()        
            stud=blog.objects.all()
            return render(request,'home.html',{'stud':stud,'home':'active'})
    else:
        return HttpResponseRedirect('/login/')        

# Contact.
def contact(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            fm=contactform(request.POST)
            if fm.is_valid():
                fm.save()
        else:
            fm=contactform()
        return render(request,'contact.html',{'fm':fm,'contact':'active'})  
    else:
        return HttpResponseRedirect('/login/')
              
# signup.
def user_signup(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            fm=signupform(request.POST)
            if fm.is_valid():
                fm.save()
                fm=signupform()
        else:
            fm=signupform()
        return render(request,'signup.html',{'fm':fm,'signup':'active'})  
    else:
        return HttpResponseRedirect('/login/')    
     
# login.
def user_login(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            fm=loginform(request=request,data=request.POST)
            if fm.is_valid():
                um=fm.cleaned_data['username']
                pw=fm.cleaned_data['password']
                user=authenticate(username=um,password=pw)
                user.save()
                group=Group.objects.get(name='editor')
                user.groups.add(group)
                messages.success(request,'congratulations!!!!')
                if user.is_authenticated:
                    login(request,user)
        else:
            fm=loginform(request) 
        return render(request,'login.html',{'fm':fm,'login':'active'})
    else:
        return HttpResponseRedirect('/home/')    

# logout.
def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
        return HttpResponseRedirect('/login/')
    else:
        return HttpResponseRedirect('/home/')    


# dashboard.
def dashboard(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            fm=blog(request.POST)
            user=fm.save()
            group=Group.objects.get(name='editor')
            user.groups.add(group)
        stud=blog.objects.all()
        user=request.user
        full_name=user.get_full_name()
        gps=user.groups.all()
        return render(request,'dashboard.html',{'stud':stud,'full_name':full_name,'groups':gps,'dashboard':'active'})
    else:
        return HttpResponseRedirect('/login/')    

# update.
def update(request,id):
    if request.user.is_authenticated:
        if request.method=='POST':
            pi=blog.objects.get(pk=id)
            form=blogform(request.POST,instance=pi) 
            if form.is_valid():
                form.save()
        else:
            pi=blog.objects.get(pk=id)
            form=blogform(instance=pi)  
        return render(request,'update.html',{'form':form,'update':'active'}) 
    else:
        return HttpResponseRedirect('/login/') 

# add.
def add(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form=blogform(request.POST)
            if form.is_valid():
                title=form.cleaned_data['title']
                desc=form.cleaned_data['desc']
                pst=blog(title=title,desc=desc)
                pst.save()
        else:
            form=blogform()  
        return render(request,'add.html',{'form':form,'add':'active'})  
    else:     
        return HttpResponseRedirect('/login/')  

# delete.
def delete(request,id):
    if request.user.is_authenticated:
        if request.method=='POST':
            pi=blog.objects.get(pk=id)
            pi.delete()
        return HttpResponseRedirect('/dashboard/')
    else:
        return HttpResponseRedirect('/login/')    