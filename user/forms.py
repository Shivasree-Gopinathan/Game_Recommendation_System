from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from user.models import UserProfile


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email address is already in use.")
        return email

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if password1 and password2:
            if password1 != password2:
                raise forms.ValidationError("The passwords do not match.")
            if len(password1) < 8:
                raise forms.ValidationError("The password must be at least 8 characters long.")
            # Add more password conditions as needed

        return cleaned_data


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'avatar', 'favourite_genre']



class CustomPasswordResetForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput)
