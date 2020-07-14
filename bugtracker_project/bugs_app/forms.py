from django import forms
from .models import Bug

class AddBugForm(forms.ModelForm):
    class Meta:
        model = Bug
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs = {
                'class': 'form-control'
            }),
            'desc': forms.TextArea(attrs = {
                'class': 'form-control'
            }),
            'priority': forms.TextInput(attrs = {
                'class': 'form-control'
            }),
            'state': forms.TextInput(attrs = {
                'class': 'form-control'
            })
        }