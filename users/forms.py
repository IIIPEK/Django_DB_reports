# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import RegionalPhoneNumberWidget

class CustomUserCreationForm(UserCreationForm):
    fullname = forms.CharField(label='ФИО', required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Email', required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    phone = PhoneNumberField(label='Телефон', required=False, widget=RegionalPhoneNumberWidget(attrs={'class': 'form-control'}, region='EE'))

    class Meta:
        model = CustomUser
        fields = ('fullname', 'email', 'phone', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.fullname = self.cleaned_data['fullname']
        user.email = self.cleaned_data['email']
        user.phone = self.cleaned_data['phone']
        if commit:
            user.save()
        return user


class CustomUserChangeForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['fullname', 'phone']
        widgets = {
            'fullname': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': RegionalPhoneNumberWidget(attrs={'class': 'form-control'}, region='EE')
        }


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
