from django import forms
from django.contrib.auth.models import User
from .models import UserProfile, PhoneNumber
from django.forms import inlineformset_factory
from django.core.exceptions import ValidationError
import re


class UserRegisterForm(forms.ModelForm):
    """Форма для реєстрації користувача"""
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password_confirm']

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise ValidationError("Username is already taken.")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("Email is already registered.")
        return email

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 8:
            raise ValidationError("Password must be at least 8 characters long.")
        if not re.search(r'[A-Z]', password):
            raise ValidationError("Password must contain at least one uppercase letter.")
        if not re.search(r'[a-z]', password):
            raise ValidationError("Password must contain at least one lowercase letter.")
        if not re.search(r'[0-9]', password):
            raise ValidationError("Password must contain at least one digit.")
        return password

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')

        if password and password_confirm and password != password_confirm:
            self.add_error('password_confirm', "Passwords do not match.")
        return cleaned_data


class UserProfileForm(forms.ModelForm):
    """Форма для профілю користувача"""
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'avatar']


class PhoneNumberForm(forms.ModelForm):
    class Meta:
        model = PhoneNumber
        fields = ['number']

PhoneNumberFormSet = inlineformset_factory(UserProfile, PhoneNumber, form=PhoneNumberForm, extra=1, can_delete=True)