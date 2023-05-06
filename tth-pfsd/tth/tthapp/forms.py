from django import forms
from .models import User, UserProfile


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']


class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['full_name', 'address']