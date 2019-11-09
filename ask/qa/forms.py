from django import forms
from qa.models import Question, Answer

class AskForm(forms.Form):
	title = forms.CharField(max_length=100)
	text = forms.CharField(widget=forms.Textarea)
	hidden = forms.CharField(widget=forms.HiddenInput())

	def clean(self):
		title = self.cleaned_data.get('title')
		text = self.cleaned_data.get('text')
#		if len(title) < 3:
#			self._errors['title'] = self.error._class(["minimum 4 symbols required"])
#		if len(text) < 10:
#			self._errors['text'] = self.error._class(["minimum 10 symbols in text required"])
		return self.cleaned_data
#		if not is_valid(self.cleaned_data):
#			raise forms.ValidationError(u'error in text', code='notvalid')

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
