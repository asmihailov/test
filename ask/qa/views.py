from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_GET
from django.http import HttpResponse, Http404, HttpResponseRedirect
from qa.models import Question 
from qa.models import Answer
from django.core.paginator import Paginator

def test(request, *args, **kwargs):
	return HttpResponse('OK')


def all_questions(request):
	questions = Question.objects.order_by('-id')
	limit = request.GET.get ('limit', 10)
	page = request.GET.get('page', '1')
	paginator = Paginator(questions, limit)
	paginator.baseurl = '/?page='
	page = paginator.page(page)
	return render(request, 'qa/all.html', {
	'questions': page.object_list,
	'title': questions.title,
	'paginator': paginator,
	'page': page})

def popular(request):
	questions = Question.objects.order_by('-rating')
	limit = request.GET.get('limit', 10)
	page = request.GET.get('page', '1')
	paginator = Paginator(questions, limit)
	paginator.baseurl = '/popular/?page='
	page = paginator.page(page)
	return render(request, 'qa/all.html', {
	'questions': page.object_list,
        'title': questions.title,
        'paginator': paginator,
        'page': page})

def one_question(request, question_id):
	questions = get_object_or_404(Question, id=question_id)
	answers = Answer.objects.filter(question=questions)
	return render(request, 'qa/question.html', {
	'questions': questions,
        'title': questions.title,
        'text': questions.text,
	'answers': answers.all()[:]})
