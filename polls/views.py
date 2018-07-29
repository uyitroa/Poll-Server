from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .custommodels import Question, Answer
from .setup import *

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

def submitAnswer(request):
	try:
		pass
	except Exception as e:
		print(e)
		return error()
