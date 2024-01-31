from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseForbidden
from .models import Post
from .forms import PostForm, UserRegistration, LoginForm
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib import messages

#------------User Authentication----------------------
def login(request):
    context = {
        'login_form': LoginForm()
    }
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = authenticate(
                request,
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                auth_login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password.')
        return render(request, "login.html", {'login_form': form})
    return render(request, "login.html", context)


def signup(request):
    context = {
        'user_form': UserRegistration(),
    }
    if request.method == "POST":
        form1 = UserRegistration(request.POST)
        if form1.is_valid():
            form1.save()
            return redirect('login')
        else:
            return render(request, "signup.html", {'user_form': form1})
    return render(request, "signup.html", context)


def logout(request):
    auth_logout(request)
    return redirect('login')


def restricted(request):
    if not request.user.is_authenticated:
        return HttpResponseForbidden("You don't have access to this page.")
    else:
        return render(request, 'restricted.html')


#-----------------------Blog Post CRUD--------------------------------------------------------
def home(request):
    posts = Post.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'home.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post': post})


def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()  
            post.user = request.user
            post.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})


def update_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PostForm(instance=post)
    return render(request, 'update_post.html', {'form': form})


def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('home')
    return render(request, 'delete_post.html', {'post': post})