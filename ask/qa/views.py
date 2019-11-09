from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_GET
from django.http import HttpResponse, Http404, HttpResponseRedirect
from qa.models import Question
from qa.models import Answer
from django.core.paginator import Paginator
from .forms import AskForm, AnswerForm
from django.views.decorators.csrf import csrf_exempt

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

#@csrf_exempt
#def answer_add(request):
#	if request.method == "POST":
#		form = AnswerForm(initial={'question': question_id})
#		return render(request, "answer_add.html", {
#		'question': question,
#		'title': question.title,
#		'text': question.text,
#		'answers': answers.all()[:],
#		'form': form,
#		})
#		post = form.save
#	url = "question"
#	adds = str(post.id)
#	return HttpResponseRedirect(url + adds)

