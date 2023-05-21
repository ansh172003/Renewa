
from django import forms
 
class Imageupload(forms.Form):
    # name = forms.CharField()
    geeks_field = forms.ImageField()