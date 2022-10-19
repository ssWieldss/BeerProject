from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class ManSignUpForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs=({'placeholder': 'Имя', 'class': 'input-data-field', 'name': 'name'})))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs=({'placeholder': 'Электронная почта', 'class': 'input-data-field', 'name': 'email'})))
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs=({'placeholder': 'Пароль', 'class': 'input-data-field', 'name': 'password',
                'minlength': 6, 'maxlength': 15})))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs=({'placeholder': 'Повторите пароль', 'class': 'input-data-field', 'name': 'password',
                'minlength': 6, 'maxlength': 15})))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class ManSignInForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs=({'placeholder': 'Имя', 'class': 'input-data-field', 'name': 'name'})))

    password = forms.CharField(widget=forms.PasswordInput(
        attrs=({'placeholder': 'Пароль', 'class': 'input-data-field', 'name': 'password',
                'minlength': 6, 'maxlength': 15})))
