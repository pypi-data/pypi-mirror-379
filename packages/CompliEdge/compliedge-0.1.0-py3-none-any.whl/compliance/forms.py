from django import forms
from .models import ComplianceChecklist, ComplianceAudit

class ComplianceChecklistForm(forms.ModelForm):
    class Meta:
        model = ComplianceChecklist
        fields = ['status', 'notes', 'due_date']
        widgets = {
            'status': forms.Select(attrs={'class': 'form-control'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'due_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

class ComplianceAuditForm(forms.ModelForm):
    class Meta:
        model = ComplianceAudit
        fields = ['framework', 'audit_date', 'findings', 'recommendations', 'completed']
        widgets = {
            'framework': forms.Select(attrs={'class': 'form-control'}),
            'audit_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'findings': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'recommendations': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'completed': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }