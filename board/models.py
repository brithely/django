from django.db import models
import datetime

# Create your models here.

class User(models.Model):
	id_email = models.CharField(max_length=100, null=False, primary_key=True)
	password = models.CharField(max_length=128, null=False)
	user_name = models.CharField(max_length=15, null=False)
	created = models.DateTimeField(auto_now_add=True)
	last_login = models.DateTimeField()

class Board(models.Model):
	num_id = models.AutoField(primary_key=True)
	cont_nm = models.CharField(max_length=100, null=False)
	content = models.TextField(null=False)
	created = models.DateTimeField(auto_now_add=True)
	created_user = models.CharField
