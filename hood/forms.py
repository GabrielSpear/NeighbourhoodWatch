from .models import Profile, Post, Hood
from django import forms


class NewProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
