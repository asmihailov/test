from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_GET
from django.http import HttpResponse, Http404, HttpResponseRedirect
from qa.models import Question
from qa.models import Answer
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import AskForm, AnswerForm, SignupForm, LoginForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse

def test(request, *args, **kwargs):
	return HttpResponse('OK')


def all_questions(request):
	questions = Question.objects.order_by('-id')
	limit = request.GET.get ('limit', 10)
	page = request.GET.get('page', '1')
	paginator = Paginator(questions, limit)
	paginator.baseurl = '/?page='
	page = paginator.page(page)
	return render(request, 'all.html', {
	'questions': page.object_list,
	'title': page.object_list,
	'paginator': paginator,
	'page': page})

def popular(request):
	questions = Question.objects.order_by('-rating')
	limit = request.GET.get('limit', 10)
	page = request.GET.get('page', '1')
	paginator = Paginator(questions, limit)
	paginator.baseurl = '/popular/?page='
	page = paginator.page(page)
	return render(request, 'all.html', {
	'questions': page.object_list,
        #'title': questions.title,
        'paginator': paginator,
        'page': page})

@csrf_exempt
def one_question(request, question_id):
	if request.method == "POST":
		return HttpResponse('200')
#		return question_add(request)
	form = AnswerForm(initial={'question': question_id})
	questions = get_object_or_404(Question, id=question_id)
	answers = Answer.objects.filter(question=questions)
	return render(request, 'question.html', {
	'questions': questions,
        'title': questions.title,
        'text': questions.text,
	'answers': answers.all()[:],
	'form': form,
	})

@csrf_exempt	
def question_add(request):
	if request.method == "POST":
		form = AskForm(request.POST)
		if not form.is_valid():
#			return HttpResponse("Bad request")
			form._user = request.user
			post = form.save()
			url = "/question/"
			adds = str(post.id)
			return HttpResponseRedirect(url + adds)
		else:
			post = form.save()
			url = "/question/"
			adds = str(post.id)
			return HttpResponseRedirect(url + adds)
	else:
		form = AskForm(request.POST)
	return render(request, "question_add.html", {'form': form})

def user_signup(request):
	if request.method == 'POST':
		form = SignupForm(request.POST)
		if form.is_valid():
			user = form.save()
			if user is not None:
				login(request, user)
				return HttpResponseRedirect('/')
	form = SignupForm()
	return render(request, 'signup.html', {'form': form})

def user_login(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			user = form.save()
			if user is not None:
				login(request, user)
				return HttpResponseRedirect('/')
	form = LoginForm()
	return render(request, 'login.html', {'form': form})

def user_logout(request):
	if request.user is not None:
		logout(request)
		return HttpResponseRedirect('/')
