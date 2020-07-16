from django import forms
from .models import Bug

class AddBugForm(forms.ModelForm):
    class Meta:
        model = Bug
        fields = ('name','desc','priority','state')
        widgets = {
            'name': forms.TextInput(attrs = {
                'class': 'form-control'
            }),
            'desc': forms.Textarea(attrs = {
                'class': 'form-control'
            }),
            'priority': forms.Select(attrs = {
                'class': 'form-control'
            }),
            'state': forms.Select(attrs = {
                'class': 'form-control'
            })
        }