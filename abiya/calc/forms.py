from.models import contact,menu,table,himg
from django import forms

class contactForm(forms.ModelForm):
    class Meta:
        model=contact
        fields='__all__'

class menuform(forms.ModelForm):
    class Meta:
        model=menu
        fields='__all__'        

class tableform(forms.ModelForm):
    class Meta:
        model=table
        fields='__all__'   
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time':forms.TimeInput(attrs={'type':'time'})
        }  

class himgform(forms.ModelForm):
    class Meta:
        model=himg
        fields='__all__'