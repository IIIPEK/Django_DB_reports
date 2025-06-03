from django import forms
from .models import Report, Alert

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['title', 'description', 'query']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'query': forms.Textarea(attrs={'class': 'form-control', 'rows': 6}),
        }


class AlertForm(forms.ModelForm):
    class Meta:
        model = Alert
        fields = ['title', 'description', 'report', 'cron']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'report': forms.Select(attrs={'class': 'form-select'}),
            'cron': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '* * * * *'}),
        }
