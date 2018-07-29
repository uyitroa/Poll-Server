from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .custommodels import Question, Answer
from .setup import global_answer_class
from .setup import global_question_class
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET
import json

# Create your views here.
def error():
	return HttpResponse("Error")

@require_GET
def getQuestion(request, ide):
	try:
		question_json = global_question_class.getQuestionById(ide)

		if question_json == None:
			return error()
		response = JsonResponse(question_json)
		response["Access-Control-Allow-Origin"] = "*"
		response["Access-Control-Allow-Methods"] = "GET, OPTIONS"
		response["Access-Control-Max-Age"] = "1000"
		response["Access-Control-Allow-Headers"] = "X-Requested-With, Content-Type"
		return response
	except Exception as e:
		print(e)
		return error()

@api_view(['POST'])
@csrf_exempt
def checkAnswer(request):
	try:
		answer_user = json.loads(request.body)
		answer_server = global_answer_class.getAnswerById(ide)
		same = 'True'
		answer_user = answer_user['answer']
		answer_server = answer_server['answer']

		for x in range(len(answer_user)):
			for y in range(len(answer_server)):
				if answer_user[x] == answer_server[x]:
					same = 'True'
					break
				else:
					same  = 'False'
			if same == 'False':
				break
		return HttpResponse(same)
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

@api_view(['POST'])
@csrf_exempt
def checkLogin(request):
	try:
		login_json = json.loads(request.body) # login_json = {'username' : 'konal', 'password' : 'idk'}
	except Exception as e:
		print(e)
		return error()
