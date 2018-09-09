from django import forms
from django.contrib.auth.models import User

from .models import Board, Comment

class BoardForm(forms.ModelForm):

	class Meta:
		model = Board
		fields = ('title', 'content',)

class UserSignForm(forms.ModelForm):
	password=forms.CharField(widget=forms.PasswordInput())
	confirm_password=forms.CharField(widget=forms.PasswordInput())

	class Meta:
		model = User
		fields = ('username', 'email', 'password',)
	
	def clean(self):
		cleaned_data = super(UserSignForm, self).clean()
		password = cleaned_data.get('password')
		confirm_password = cleaned_data.get('confirm_password')

		if password != confirm_password:
			raise forms.ValidationError(
				"password and confirm_password does not match"
			)
		

class CommentForm(forms.ModelForm):
	
	class Meta:
		model = Comment
		fields = ('comment',)
