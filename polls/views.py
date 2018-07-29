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
def getAnswer(request, ide): # ide is questionID
	try:
		answer_json = global_answer_class.getAnswersByQuestionId(ide) # get the users answers.
		question_json = global_question_class.getQuestionById(ide) # get the question of the answer
		answers = question_json['answers'] # get answer choices
		print(question_json)
		data = {}
		data["questionID"] = question_json['id']
		data["text"] = question_json['text']
		data["text"] = question_json['text']
		data["images"] = question_json['images']
		data["video"] = question_json['video']
		list_answers = [] # data output
		for a in range(len(answers)):
			list_answers.append({'value' : answers[a], 'users' : []})# add a list user for each field, for example {'non' : [], 'oui' : []}
			for j in answer_json:
				if a in j['answer']: # if an answer is chosen by the user
					list_answers[a]['users'].append(j['userID']) # then append it to the field for example {'non' : ['u1'], 'oui' : []}
		data["answers"] = list_answers
		print(data)
		return JsonResponse(data, safe = False) # return data
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
