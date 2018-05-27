from django.shortcuts import render
from . models import Hood, Business, Profile, Post
from django.contrib.auth.decorators import login_required
from . forms import NewProfileForm, NewPostForm, NewHoodForm
from django.contrib.auth.models import User

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


@login_required(login_url='/accounts/register')
def update_profile(request):
    profile = Profile.objects.all()
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.save()
            return redirect('profile')
    else:
        form = ProfileForm()
    return render(request, 'all-watch/update_profile.html', {"form": form})


@login_required(login_url='/accounts/register')
def post(request):
    post = Post.objects.all()
    return render(request, 'all-watch/post.html', {"post": post})


@login_required(login_url='/accounts/register')
def new_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post = current_user
            post.save()
            return redirect('/')
    else:
        form = NewPostForm()
    return render(request, 'all-watch/new-post.html', {"form": form})


@login_required(login_url='/accounts/register')
def hood(request):
    hood = Hood.objects.all()
    return render(request, 'all-watch/hood.html', {"hood": hood})


@login_required(login_url='/accounts/register')
def update_hood(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewHoodForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post = current_user
            post.save()
            return redirect('/')
    else:
        form = NewPostForm()
    return render(request, 'all-watch/update_hood.html', {"form": form})


@login_required(login_url='/accounts/register')
def business(request):
    business = Business.objects.all()
    return render(request, 'all-watch/business.html', {"business": business})


@login_required(login_url='/accounts/register')
def search_results(request):
    if 'business' in request.GET and request.GET["business"]:
        search_term = request.GET.get('business')
        searched_business = Business.searched_business(search_term)

        message = f"{search_term}"

        return render(request, 'all-watch/search.html', {"message": message, "business": searched_business})
    else:
        message = "you haven't searched for any term"
        return render(request, 'all-watch/search.html', {"message": message})
