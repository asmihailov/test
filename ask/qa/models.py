from django.contrib.auth.models import User

class Question(django.contrib.auth.models.User):
	title = models.CharField(max_length=255)
	text = models.TextField()
	added_at = models.DateTimeField();
