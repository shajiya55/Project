from django import forms
from.models import proom,Contact,Reserve

class proomforms(forms.ModelForm):
    class Meta:
        model=proom
        fields='__all__'

class Contactform(forms.ModelForm):
    class Meta:
        model=Contact
        fields='__all__'      

class ReserveForm(forms.ModelForm):
    class Meta:
        model=Reserve
        fields='__all__'
        widgets = {
            'Adate':forms.DateInput(attrs={'type': 'date'}),
            'ddate':forms.DateInput(attrs={'type':'date'})
        }  
        labels={'Adate':'Arrival Date','ddate':'Departure Date'}
