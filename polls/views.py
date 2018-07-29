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
		ide = answer_user['id']
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