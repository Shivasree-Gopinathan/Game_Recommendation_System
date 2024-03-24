from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect,reverse
from django.contrib.auth import authenticate, login
from .forms import SignUpForm, LoginForm, UserProfileForm
from .models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.contrib import messages

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the user to the database
            UserProfile.objects.create(user=user)
            login(request, user)  # Log in the user after successful signup
            return redirect('login')  # Redirect to signup success page
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"Error in {field}: {error}")
    else:
        form = SignUpForm()
    return render(request, 'user/signup.html', {'form': form})
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


def forgot_password(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            user = User.objects.get(username=username)
            if user is not None:
                # Generate token
                uid = urlsafe_base64_encode(force_bytes(user.pk))
                token = default_token_generator.make_token(user)

                # Construct reset password URL
                reset_url = request.build_absolute_uri(
                    reverse('reset_password_confirm', kwargs={'uidb64': uid, 'token': token})
                )

                # Send reset password email to user
                send_mail(
                    'Reset Your Password',
                    f'Please click the following link to reset your password: {reset_url}',
                    'from@example.com',
                    [user.email],
                    fail_silently=False,
                )

                # Redirect to a page informing the user to check their email
                return render(request, 'password_reset_email_sent.html')
    else:
        form = PasswordResetForm()
    return render(request, 'forgot_password.html', {'form': form})


def reset_password_confirm(request, uidb64, token):
    # Decode the user ID from uidb64
    from django.utils.http import urlsafe_base64_decode
    from django.contrib.auth.tokens import default_token_generator
    from django.utils.encoding import force_text
    from django.core.exceptions import ValidationError
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist, ValidationError):
        user = None

    # Check if user and token are valid
    if user is not None and default_token_generator.check_token(user, token):
        if request.method == 'POST':
            # Change password for the authenticated user
            password = request.POST.get('password')
            user.set_password(password)
            user.save()

            # Log the user in with the new password
            user = authenticate(username=user.username, password=password)
            login(request, user)

            # Redirect to a success page
            return render(request, 'password_reset_complete.html')
    else:
        # Redirect to an error page if user or token is invalid
        return render(request, 'password_reset_invalid.html')