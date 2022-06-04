from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Profile


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email')

class ProfileForm(forms.ModelForm):
    
    class Meta:

        model = Profile
        fields = '__all__'
        # widgets = { 'username': forms.Select(attrs={'disabled':'disabled'})}