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
def submitAnswer(request):
	try:
		answer_user = json.loads(request.body)
		ide = answer_user['id']
		answer_server = global_answer_class.getAnswerById(ide)


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
