from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .setup import global_account_class, global_answer_class, global_question_class
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
		data_json = json.loads(request.body)
		questionID = data_json['questionID']
		answer_list = global_answer_class.getAnswersByQuestionId(questionID)
		print(answer_list)
		return JsonResponse(answer_list, safe = False)
	except Exception as e:
		print(e)
		return error()

def getAnswer(request, ide):
	try:
		answer_json = global_answer_class.getAnswersByQuestionId(ide)
		return JsonResponse(answer_json, safe = False)
	except Exception as e:
		print(e)
		return error()

@api_view(['POST'])
@csrf_exempt
def checkLogin(request):
	try:
		login_json = json.loads(request.body)  # login_json = {'username' : 'konal', 'password' : 'idk'}
		account_login = global_account_class.userLogin(login_json)
		if account_login == True:
			return HttpResponse("True")
		else:
			return HttpResponse("False")
	except Exception as e:
		print(e)
		return error()
