from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
      username = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder": "Your username",
        "class" :"w-full py-4 px-6 rounded-xl"
    }))
      password = forms.CharField(widget=forms.PasswordInput(attrs={
        "placeholder": "Your password",
        "class" :"w-full py-4 px-6 rounded-xl"
    }))

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields =("username", "email", "password1", "password2")

    username= forms.CharField(widget=forms.TextInput(attrs={
        "placeholder": "Your username",
        "class" :"w-full py-4 px-6 rounded-xl"
    }))

    email = forms.CharField(widget=forms.EmailInput(attrs={
        "placeholder": "Your email address",
        "class" :"w-full py-4 px-6 rounded-xl"
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        "placeholder": "Your password",
        "class" :"w-full py-4 px-6 rounded-xl"
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
         "placeholder": "Confirm password",
        "class" :"w-full py-4 px-6 rounded-xl"
    }))

class AccountSettingsForm(forms.Form):
    new_username = forms.CharField(max_length=150, required=False, widget=forms.TextInput(attrs={'placeholder': "Current Username"}))
    new_email = forms.EmailField(required=False, widget=forms.TextInput())
    new_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter new password'}), required=False)
    confirm_new_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm new password'}), required=False)

    def clean(self):
        cleaned_data = super().clean()
        new_password = cleaned_data.get('new_password')
        confirm_new_password = cleaned_data.get('confirm_new_password')

        if new_password and confirm_new_password:
            if new_password != confirm_new_password:
                raise forms.ValidationError("Passwords do not match")

        return cleaned_data



