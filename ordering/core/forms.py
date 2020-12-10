from django import forms
from.models import limit,market,stop

class limitform(forms.ModelForm):
    class Meta:
        model=limit
        fields='__all__'

class marketform(forms.ModelForm):
    class Meta:
        model=market
        fields='__all__'

class stopform(forms.ModelForm):
    class meta:
        model=stop 
        fields='__all__'              