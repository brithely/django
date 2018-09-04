from django import forms
from django.contrib.auth.models import User

from .models import Board, Comment

class BoardForm(forms.ModelForm):

	class Meta:
		model = Board
		fields = ('title', 'content',)

class UserSignupForm(forms.ModelForm):

	class Meta:
		model = User
		fields = ('username', 'password', 'email',)
		widgets = {'password': forms.PasswordInput()}

class UserSigninForm(forms.ModelForm):

	class Meta:
		model = User
		fields = ('username', 'password',)
		widgets = {'password': forms.PasswordInput()}

class CommentForm(forms.ModelForm):
	
	class Meta:
		model = Comment
		fields = ('comment',)
