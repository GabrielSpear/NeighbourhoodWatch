from .models import Profile, Post, Hood
from django import forms


class NewProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']


class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['user']
