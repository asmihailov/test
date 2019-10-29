from django.db import models
from django.contrib.auth.models import User 

class QuestionManager(models.Manager):
	def new(self):
		return self.order_by('-added_at')
	def popular(self):
		return self.order_by('-rating')

class Question(models.Model):
	objects = QuestionManager()
	title = models.CharField(max_length=50)
	text = models.TextField(max_length=100)
	added_at = models.DateTimeField(blank = True, auto_now_add=True)
	rating = models.IntegerField(default=0)
	author = models.ForeignKey(User, on_delete=models.PROTECT)
	likes = models.ManyToManyField(User, related_name="qlikes")
	def __unicode__(self):
		return self.title
class Answer(models.Model):
	text = models.TextField(max_length=100)
	added_at = models.DateTimeField(auto_now_add=True)
	question = models.ForeignKey(Question, blank=True, related_name="Aquestion", on_delete=models.PROTECT)
	author = models.ForeignKey(User, related_name="Aauthor", on_delete=models.PROTECT)
	def __unicode__(self):
		return self.text

