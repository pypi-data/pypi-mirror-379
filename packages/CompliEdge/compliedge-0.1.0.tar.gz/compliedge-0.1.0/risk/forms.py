from django import forms
from .models import Risk, RiskMitigation, RiskReview, RiskCategory

class RiskForm(forms.ModelForm):
    class Meta:
        model = Risk
        fields = ['title', 'description', 'category', 'likelihood', 'impact', 'mitigation_plan', 'due_date']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'likelihood': forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'max': 5}),
            'impact': forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'max': 5}),
            'mitigation_plan': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'due_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

class RiskMitigationForm(forms.ModelForm):
    class Meta:
        model = RiskMitigation
        fields = ['action', 'description', 'due_date']
        widgets = {
            'action': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'due_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

class RiskReviewForm(forms.ModelForm):
    class Meta:
        model = RiskReview
        fields = ['comments']
        widgets = {
            'comments': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }