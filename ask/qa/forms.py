from django import forms
from qa.models import Question, Answer

class AskForm(forms.Form):
	title = CharField(max-length=100)
	text = CharField(widget=forms.TextArea)

	def clean(self):
		text = self.cleaned_data['text']
		if not text:
			raise forms.ValidationError('question text is not correct')
		return text
	
	def save(self):
		question = Question(**self.cleaned_data)
		question.save()
		return question

class AnswerForm(forms.Form):
	text = CharField(widget=forms.TextArea)
	question = IntegerField()


	def save(self):
		answer = Answer(**self.cleaned_data)
		answer.save()
		return answer
