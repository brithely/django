from django.db import models
from django.contrib import admin
from django.conf import settings
import datetime

# Create your models here.

class Board(models.Model):
	num_id = models.AutoField(primary_key=True)
	title = models.CharField(max_length=100, null=False)
	content = models.TextField(null=False)
	created = models.DateTimeField(auto_now_add=True)
	created_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

	def __str__(self):
		return self.title

class Comment(models.Model):
	num_board_id = models.ForeignKey(Board, on_delete=models.CASCADE)
	num_com_id = models.AutoField(primary_key=True)
	comment = models.CharField(max_length=255, null=False)
	created = models.DateTimeField(auto_now_add=True)
	created_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	
	def __str__(self):
		return self.num_board_id
