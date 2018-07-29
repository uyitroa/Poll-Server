from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .setup import global_account_class, global_answer_class, global_question_class
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET
import json
import hashlib

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
		return response
	except Exception as e:
		print(e)
		return error()

@api_view(['POST'])
@csrf_exempt
def submitAnswer(request):
	try:
		data_json = json.loads(request.body)

		global_answer_class.createAnswer(data_json)

		questionID = data_json['questionID']
		answer_list = global_answer_class.getAnswersByQuestionId(questionID)
		print(answer_list)
		return JsonResponse(answer_list, safe = False)
	except Exception as e:
		print(e)
		return error()

@require_GET
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
		login_json = json.loads(request.body)
		hash = hashlib.md5(login_json["password"].encode())
		hash = hash.hexdigest()
		login_json["password"] = hash
		account_login = global_account_class.userLogin(login_json)
		if account_login == True:
			return HttpResponse("True")
		else:
			return HttpResponse("False")
	except Exception as e:
		print(e)
		return error()
	
@api_view(['POST'])
@csrf_exempt
def newAccount(request):
	form_json = json.loads(request.body) # form_json = {"username" : "asdf", "password" : "af"}
	hash = hashlib.md5(form_json["password"].encode())
	hash = hash.hexdigest()
	form_json["password"] = hash
	global_account_class.createAccount(form_json)