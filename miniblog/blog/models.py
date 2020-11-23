from django.db import models
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

# blog model.
class blog(models.Model):
    title=models.CharField(max_length=70)
    desc=models.TextField()
    
# contact model.
class contact(models.Model):
    name=models.CharField(max_length=10)
    email=models.EmailField(max_length=254) 
    message=models.TextField()   

# signup model.
class signupforms(UserCreationForm):
    fields=['username','first_name','last_name']

# login model.
class loginform(AuthenticationForm):
    fields=['username','password']