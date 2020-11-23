from django import forms
from .models import contact,blog
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User

class contactform(forms.ModelForm):
    name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),error_messages={'required':'please enter your name'})
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}),error_messages={'required':'please enter your email '})
    message=forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}),error_messages={'required':'please enter your messages'})
    class Meta:
        model=contact
        fields=['name','email','message']
        

class blogform(forms.ModelForm):
    class Meta:
        model=blog
        fields=['title','desc']
        title=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
              

class signupform(UserCreationForm):
    username=forms.CharField(error_messages={'required':'please enter your username'},widget=forms.TextInput(attrs={'class':'form-control'}))
    first_name=forms.CharField(error_messages={'required':'please enter your firstname'},widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name=forms.CharField(error_messages={'required':'please enter your lastname'},widget=forms.TextInput(attrs={'class':'form-control'}))
    password1=forms.CharField(label='password',error_messages={'required':'please enter your password'},widget=forms.PasswordInput(attrs={'class':'form-control'}))  
    password2=forms.CharField(label='password(confirmation)',error_messages={'required':'please confirm your password'},widget=forms.PasswordInput(attrs={'class':'form-control'}))  
    class Meta:
        model=User 
        fields=['username','first_name','last_name']      
        
class loginform(AuthenticationForm):
    class Meta:
        fields=['username','password'] 
        