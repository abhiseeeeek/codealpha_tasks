# socialapp/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from .models import Post, Comment, Profile
from django.contrib.auth.views import LogoutView
from django.shortcuts import redirect

class MyLogoutView(LogoutView):
    http_method_names = ['get', 'post']

def accounts_profile_redirect(request):
    return redirect('home')  # or any other view name you want

@login_required
def home(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'socialapp/home.html', {'posts': posts})

@login_required
def create_post(request):
    if request.method == "POST":
        content = request.POST.get('content')
        Post.objects.create(author=request.user, content=content)
        return redirect('home')
    return render(request, 'socialapp/create_post.html')

@login_required
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    # Toggle like/unlike
    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required
def add_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == "POST":
        content = request.POST.get('content')
        Comment.objects.create(post=post, author=request.user, content=content)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required
def profile_view(request, username):
    user_obj = get_object_or_404(User, username=username)
    profile = user_obj.profile  # thanks to the OneToOne relation and signals
    posts = Post.objects.filter(author=user_obj).order_by('-created_at')
    context = {
        'profile_user': user_obj,
        'profile': profile,
        'posts': posts,
    }
    return render(request, 'socialapp/profile.html', context)

@login_required
def follow_toggle(request, username):
    target_user = get_object_or_404(User, username=username)
    target_profile = target_user.profile
    current_profile = request.user.profile
    if current_profile != target_profile:
        # Check if already following
        if current_profile in target_profile.followers.all():
            target_profile.followers.remove(current_profile)
        else:
            target_profile.followers.add(current_profile)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
