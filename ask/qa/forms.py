from django import forms
from qa.models import Question, Answer

class AskForm(forms.Form):
	title = forms.CharField(max_length=100)
	text = forms.CharField(widget=forms.Textarea)
	hidden = forms.CharField(widget=forms.HiddenInput())

	def save(self):
		questions = Question(**self.cleaned_data)
		questions.author_id = 1
		questions.save()
		return questions

class AnswerForm(forms.Form):
	text = forms.CharField(widget=forms.Textarea)
	question = forms.IntegerField()


	def save(self):
		answer = Answer(**self.cleaned_data)
		answer.save()
		return answer
