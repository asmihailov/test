from django.db import models
from django.contrib.auth.models import User 

class Question(models.Model):
	title = models.CharField(max_length=50)
	text = models.TextField(max_length=100)
	added_at = models.DateTimeField(blank = True, auto_now_add=True)
	rating = models.IntegerField(default=0)
	author = models.CharField(max_length=20)
	likes = models.ForeignKey(User, null=True)
	def __unicode__(self):
		return self.title
class Answer(models.Model):
	text = models.CharField(max_length=100)
	added_at = models.DateTimeField(auto_now_add=True)
	question = models.ForeignKey(Question, null=True)
	author = models.ForeignKey(Question, null=True, on_delete=models.SET_NULL)
	def __unicode__(self):
		return self.text
	class QuestionManager(models.Manager):
		def new(self):
			return self.order_by('-added_at')
		def popular(self):
			return self.order_by('-rating')
