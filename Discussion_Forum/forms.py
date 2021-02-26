from django.forms import ModelForm
from .models import *
from django import forms

"""Форма Вопросов"""


class CreateInForum(forms.ModelForm):

    class Meta:
        model = forum
        fields = ('name','email','topic', 'description',  'opisanie','user_photo', 'username')


class ReviewForm(forms.ModelForm):
    """Форма отзывов"""
    class Meta:
        model = Reviews
        fields = ("name",  "text", "user_photo",'email')

class CallForm(forms.ModelForm):

    class Meta:
        model = Call
        fields  = '__all__'

"""Форма Входа"""


class LoginForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'input100', 'type': 'text', 'name': 'name', 'placeholder': 'Type your username', 'value': '{{ request.user.get_full_name }}'}))
    text = forms.CharField(widget=forms.TextInput(attrs={'class': 'input100', 'type': 'text', 'name': 'text', 'placeholder': 'Type your username'}))
    user_photo = forms.CharField(widget=forms.TextInput(attrs={'class': 'input100', 'type': 'text', 'name': 'user_photo', 'placeholder': 'Type your username', 'value': '{{ profile.photo.url }}'}))
