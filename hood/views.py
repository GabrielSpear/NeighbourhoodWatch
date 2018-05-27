from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
@login_required(login_url='/accounts/register')
def index(request):
    post = Post.get_post()
    hood = Hood.get_hood()
    profile_form = NewProfileForm
    # profile = Profile.objects.all()
    return render(request, 'index.html', {"post": post, "profile_form": NewProfileForm, "hood": hood})
