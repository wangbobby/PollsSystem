from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.template import loader
from django.http import HttpResponse
from .models import Question

def index(request):
	# print(request)
	# print("Path: " + request.path)
	# print(request.method)
	# print(request.COOKIES)
	# print(request.session)
	# print(request.FILES)
	# print(request.GET)
	# print(request.POST)
	# return HttpResponse("Hello, world. You're at the polls index")
	"""
	latest_question_list = Question.objects.order_by('-pub_date')[0:5]
	# output = ', '.join([q.question_text for q in latest_question_list])
	template = loader.get_template('polls/index.html')
	context = {
		'latest_question_list': latest_question_list
	}
	# return HttpResponse(output)
	return HttpResponse(template.render(context, request))
	"""
	latest_question_list = Question.objects.order_by('-pub_date')[0:5]
	context = {'latest_question_list': latest_question_list}
	return render(request, 'polls/index.html', context)

# def detail(request, question_id):
# 	return HttpResponse("You're looking at question %s." %question_id)

def detail(request, question_id):
	print(request)
	# return HttpResponse("You're looking at question %s." % question_id)
	"""
	try:
		question = Question.objects.get(pk=question_id)
	except Question.DoesNotExist:
		raise Http404("Qustion does not exist")
	"""
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
	print(request)
	response = "You're looking at the results of question %s."
	return HttpResponse(response %question_id)

def vote(request, question_id):
	print(request)
	return HttpResponse("You're voting on question %s." %question_id)