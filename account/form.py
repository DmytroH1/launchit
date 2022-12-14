from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class RegisterUserForm(UserCreationForm):
	"""Форма зворотнього зв'язку"""
	username = forms.CharField()
	email = forms.EmailField()
	password1 = forms.CharField()
	password2 = forms.CharField()

	class Meta:
		model = User
		fields = ('username', 'email', 'password1', 'password2')
