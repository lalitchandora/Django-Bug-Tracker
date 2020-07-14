from django import forms
from .models import Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs = {
                'class': 'form-control'
            }),
            'organization_name': forms.TextInput(attrs = {
                'class': 'form-control'
            }),
            'technology': forms.TextInput(attrs = {
                'class': 'form-control'
            })
        }