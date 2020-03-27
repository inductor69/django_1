from django import forms

class LoginForm(forms.Form):
    user_name= forms.CharField(max_length=100)
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)
    