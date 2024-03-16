from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import SignUpForm, LoginForm, UserProfileForm
from .models import UserProfile


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the user to the database

            UserProfile.objects.create(user=user)
            login(request, user)  # Log in the user after successful signup
            return redirect('login')  # Redirect to signup success page
    else:
        form = SignUpForm()
    return render(request, 'user/signup.html', {'form': form})
def signup_success(request):
    return render(request, 'user/signup_success.html')

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'user/login.html', {'form': form})

def login_success(request):
    return render(request, 'user/login_success.html')


@login_required
def view_profile(request):
    user_profile = request.user.userprofile
    return render(request, 'user/view_profile.html', {'user_profile': user_profile})


@login_required
def edit_profile(request):
    if request.method == 'POST':
        # print(request.POST)
        form = UserProfileForm(request.POST, request.FILES, instance=request.user.userprofile)
        if form.is_valid():
            form.save()
            return redirect('view_profile')  # Redirect to the profile page after editing
        else:
            print("Form errors:", form.errors)
    else:
        form = UserProfileForm(instance=request.user.userprofile)
    return render(request, 'user/edit_profile.html', {'form': form})

