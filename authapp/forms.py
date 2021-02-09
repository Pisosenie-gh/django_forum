from django import forms
from .models import Profile
from django.contrib.auth.models import User

'''Форма Логина'''


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input100', 'type': 'text', 'name': 'username', 'placeholder': 'Введите  логин'}))
    password = forms.CharField(widget=forms.TextInput(attrs={'class': 'input100', 'type': 'password', 'name': 'password', 'placeholder': 'Введите  пароль'}))


'''Форма Регистрации'''


class RegistrationForm(forms.Form):
    firstname = forms.CharField(widget=forms.TextInput(attrs={'class': 'input100', 'type': 'text', 'name': 'firstname', 'placeholder': 'Введите  имя'}))
    lastname = forms.CharField(widget=forms.TextInput(attrs={'class': 'input100', 'type': 'text', 'name': 'lastname', 'placeholder': 'Введите  фамилию'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'input100', 'type': 'email', 'name': 'email', 'placeholder': 'Введите  email'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input100', 'type': 'text', 'name': 'username', 'placeholder': 'Введите  логин'}))
    password = forms.CharField(widget=forms.TextInput(attrs={'class': 'input100', 'type': 'password', 'name': 'password', 'placeholder': 'Введите  пароль'}))
    confirm_password = forms.CharField(widget=forms.TextInput(attrs={'class': 'input100', 'type': 'password', 'name': 'confirm-password', 'placeholder': 'Введите  пароль повторно'}))


'''Форма редакта профиля'''


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


'''Форма редакта профиля 2'''


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('date_of_birth', 'photo')



'''Форма  профиля 2'''


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('date_of_birth', 'photo','user')