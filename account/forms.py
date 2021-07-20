from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError
from django.forms.widgets import EmailInput, PasswordInput, TextInput
from django.contrib.auth.backends import ModelBackend

class RegistrationForm(UserCreationForm):
    username = forms.CharField(widget=TextInput(attrs={'placeholder': 'Username'}))
    email = forms.CharField(widget=EmailInput(attrs={'placeholder': 'Email'}))
    password1 = forms.CharField(widget=PasswordInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(widget=PasswordInput(attrs={'placeholder': 'Confirm password'}))

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise ValidationError('This email already exists')
        return email

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class CustomLoginForm(AuthenticationForm):
    username = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(email=username)
        except UserModel.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                return user
        return None