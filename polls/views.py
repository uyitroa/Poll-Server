from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .custommodels import Question, Answer
from .setup import global_answer_class
from .setup import global_question_class
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def error():
	return HttpResponse("Error")

def getQuestion(request, ide):
	try:
		question_json = global_question_class.getQuestionById(ide)
		return JsonResponse(question_json)
	except Exception as e:
		print(e)
		return error()

@api_view(['POST'])
@csrf_exempt
def submitAnswer(request):
	try:
		pass
	except Exception as e:
		print(e)
		return error()

def getAnswer(request, ide):
	try:
		answer_json = global_answer_class.getAnswerById(ide)
		return JsonResponse(answer_json)
	except Exception as e:
		print(e)
		return error()
