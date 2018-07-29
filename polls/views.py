from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .setup import global_account_class, global_answer_class, global_question_class
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET
import json
import hashlib

# Create your views here.
def error(error_message = "Error"):
	return HttpResponse(error_message)

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

		return HttpResponse('True')
	except Exception as e:
		print(e)
		return error('False')

@require_GET
def getAnswer(request, ide):
	try:
		answer_json = global_answer_class.getAnswersByQuestionId(ide)
		question_json = global_question_class.getQuestionById(ide)
		answers = question_json['answers']

		response = {}
		for a in answers:
			response[a] = []
			for j in answer_json:
				if a in j['answer']:
					response[a].append(j['userID'])
		return JsonResponse(response)
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
	try:
		form_json = json.loads(request.body) # form_json = {"username" : "asdf", "password" : "af"}
		hash = hashlib.md5(form_json["password"].encode())
		hash = hash.hexdigest()
		form_json["password"] = hash
		global_account_class.createAccount(form_json)
	except Exception as e:
		print(e)
		return error()
