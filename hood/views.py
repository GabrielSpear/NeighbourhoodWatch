from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . forms import NewProfileForm, NewPostForm, NewHoodForm


# Create your views here.
@login_required(login_url='/accounts/register')
def index(request):
    post = Post.get_post()
    hood = Hood.get_hood()
    profile_form = NewProfileForm
    # profile = Profile.objects.all()
    return render(request, 'index.html', {"post": post, "profile_form": NewProfileForm, "hood": hood})


@login_required(login_url='/accounts/register')
def profile(request, user_id):
    current_user = request.user
    profile = Profile.objects.all()
    post = Post.objects.filter(profile__id=user_id)
    # post_profile=Post.objects.get(id=user_id)

    return render(request, 'all-watch/profile.html', {"current_user": current_user, "profile": profile, "post": post})
