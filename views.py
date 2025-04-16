from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post, Comment, Like
from .forms import PostForm, CommentForm
from django.utils import timezone

@login_required
def dashboard_view(request):
    posts = Post.objects.filter(user=request.user).order_by('-timestamp')
    return render(request, 'dashboard/dashboard.html', {'posts': posts})

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.timestamp = timezone.now()
            post.save()
            return redirect('dashboard')
    else:
        form = PostForm()
    return render(request, 'dashboard/create_post.html', {'form': form})

@login_required
def comment_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.timestamp = timezone.now()
            comment.save()
            return redirect('dashboard')
    else:
        form = CommentForm()
    return render(request, 'dashboard/comment_post.html', {'form': form, 'post': post})

@login_required
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    existing_like = Like.objects.filter(post=post, user=request.user)
    if not existing_like.exists():
        Like.objects.create(post=post, user=request.user)
    return redirect('dashboard')
