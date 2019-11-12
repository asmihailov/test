from django import forms
from qa.models import Question, Answer

class AskForm(forms.Form):
	title = forms.CharField(max_length=100)
	text = forms.CharField(widget=forms.Textarea)
	hidden = forms.CharField(widget=forms.HiddenInput())

	def clean(self):
		title = self.cleaned_data.get('title')
		text = self.cleaned_data.get('text')
		return self.cleaned_data

	def save(self):
#		questions = Question(**self.cleaned_data)
#		questions.author_id = 1
#		questions.save()
#		return questions

		if self._user.is_anonymous():
			self.cleaned_data['author_id'] = 1
		else:
			self.cleaned_data['author'] = self._user
			question = Question(**self.cleaned_data)
			question.save()
		return question

class AnswerForm(forms.Form):
	text = forms.CharField(widget=forms.Textarea)
	question = forms.IntegerField()


	def save(self):
		self.cleaned_data['question'] = get_object_or_404(Question,pk=self.cleaned_data['question'])
		if self._user.is_anonymous():
			self.cleaned_data['author_id'] = 1
		else:
			self.cleaned_data['author'] = self._user
			answer = Answer(**self.cleaned_data)
			answer.save()
		return answer

class SignupForm(forms.Form):
	username = forms.CharField(max_length=100)
	email = forms.EmailField()
	password = forms.CharField(widget=forms.PasswordInput)

	def clean_username(self):
		username = self.cleaned_data['username']
		if username.strip()=='' :
			raise forms.ValidationError('Username is empty', code='validation_error')
		return username
	
	def clean_password(self):
		password = self.cleaned_data['password']
                if password.strip() == '':
                	raise forms.ValidationError('Password is empty', code='validation error')
                return password

	def clean_email(self):
		email = self.cleaned_data['email']
		if email.strip() == '':
			raise forms.ValidationError('Email is empty', code='validation error')
		return email
	
	def save(self):
		user = User.objects.create_user(**self.cleaned_data)
		user.save()
		auth = authenticate(**self.cleaned_data)
		return auth

class LoginForm(forms.Form):
	username = forms.CharField(max_length=100)
	password = forms.CharField(widget=forms.PasswordInput)
        
	def clean_username(self):
		username = self.cleaned_data['username']
		if username.strip() == '':
			raise forms.ValidationError('Username is empty', code='validation error')
		return username
                                                                
	def clean_password(self):
		password = self.cleaned_data['password']
		if password.strip() == '':
			raise forms.ValidationError('Password is empty', code='validation error')
		return password

	def save(self):
		auth = authenticate(**self.cleaned_data)
		return auth
