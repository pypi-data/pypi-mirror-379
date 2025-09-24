from django import forms
from .models import Policy, PolicyComment

class PolicyForm(forms.ModelForm):
    class Meta:
        model = Policy
        fields = ['title', 'description', 'content', 'status']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }

class PolicyCommentForm(forms.ModelForm):
    class Meta:
        model = PolicyComment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Add your comment here...'}),
        }