from utilities.models.mixins import TimeStampedModel
from django.contrib import admin
from django.conf import settings
import datetime

# Create your models here.

class Board(TimeStampedModel):
	title = models.CharField(max_length=100, null=False)
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	text = models.TextField(null=False)

	def __str__(self):
		return self.title

class Comment(TimeStampedModel):
	board = models.ForeignKey(Board, on_delete=models.CASCADE)
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	text = models.CharField(max_length=255, null=False)
	
	def __str__(self):
		return self.num_board_id

class Reply(TimeStampedModel):
	comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	text = models.CharField(max_length=255, null=False)
