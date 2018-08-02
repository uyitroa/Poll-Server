from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .setup import global_account_class, global_answer_class, global_question_class
from .setup import *
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET
import json
import hashlib
from pymongo import cursor

# Create your views here.
def output(error_message = "False"):
	return JsonResponse({'update' : error_message})

@require_GET
def getQuestion(request, ide):
	try:
		question_json = global_question_class.getDictById(ide)

		if question_json == None:
			return output('False')
		response = JsonResponse(question_json)
		return response
	except Exception as e:
		print(e)
		return output('False')

@api_view(['POST'])
@csrf_exempt
def submitAnswer(request):
	try:
		data_json = json.loads(request.body.decode("utf-8"))

		global_answer_class.create(data_json)
		return JsonResponse({'update' : True})
	except Exception as e:
		print(e)
		return JsonResponse({'update' : False})

@api_view(['POST'])
@csrf_exempt
def submitQuestion(request):
	try:
		data_json = json.loads( request.body.decode('utf-8') )
		global_question_class.create(data_json)

		return output('True')
	except Exception as e:
		print(e)
		return output('False')

@api_view(['POST'])
@crsf_exempt
def updateQuestion(request):
	try:
		data_json = json.loads(request.body.decode("utf-8"))
		global_question_class.update(data_json)
		return output('True')
	except Exception as e:
		print(e)
		return output('False')

def deleteQuestion(request):
	try:
		data_json = json.loads(request.body.decode("utf-8"))
		global_question_class.delete(data_json)
		return output('True')
	except Exception as e:
		print(e)
		return output('False')

@require_GET
def getAnswer(request, ide): # ide is questionID
	try:
		answer_json = global_answer_class.getDictById(ide) # get the users answers.
		question_json = global_question_class.getDictById(ide) # get the question of the answer
		answers = question_json['answers'] # get answer choices
		data = {}
		data["questionID"] = question_json['id']
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
		return output('False')

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
		return output('False')

@api_view(['POST'])
@csrf_exempt
def newAccount(request):
	try:
		form_json = json.loads(request.body) # form_json = {"username" : "asdf", "password" : "af"}
		hash = hashlib.md5(form_json["password"].encode())
		hash = hash.hexdigest()
		form_json["password"] = hash
		global_account_class.create(form_json)
	except Exception as e:
		print(e)
		return output('False')

@require_GET
def getCreatorQuestionByStatus(request, creatorID, status):
	try:
		cursor = global_question_class.data.find({'creatorID' : creatorID, 'status' : status})
		cursorList = []
		for x in range(0, cursor.count(), 1):
			dico = cursor[x]
			dico['_id'] = ''
			cursorList.append(dico)
		return JsonResponse(cursorList, safe = False)
	except Exception as e:
		print(e)
		return output('False')

@require_GET	
def getQuestionsByCreatorId(request, creatorID):
	try:
		cursor = global_question_class.data.find({"creatorID" : creatorID})
		cursorList = []
		for x in range(0, cursor.count(), 1):
			dico = cursor[x]
			dico['_id'] = ''
			cursorList.append(dico)
		return JsonResponse(cursorList, safe = False)
	except Exception as e:
		print(e)
		return output('False')

@require_GET
def getQuestionsByUserId(request, userID):
	try:
		cursor = global_answer_class.data.find({"userID" : userID})
		cursorList = []
		for x in range(0, cursor.count(), 1):
			dico = cursor[x]
			dicte = global_question_class.data.find_one({"id" : dico["questionID"]})
			dicte['_id'] = ''
			cursorList.append(dicte)
		return JsonResponse(cursorList, safe = False)
	except Exception as e:
		print(e)
		return output('False')

def getUserByQuestionText(request, text):
	try:
		dict_questions = global_question_class.data.find_one({"text" : text})
		dict_id = dict_questions["id"]
		questionID = dict_id
		cursorList = []
		cursor_answers = global_answer_class.data.find({"questionID" : questionID})
		for x in range(0, cursor_answers.count(), 1):
			dico = cursor_answers[x]
			cursorList.append(dico["userID"])
		return JsonResponse(cursorList, safe = False)
	except Exception as e:
		print(e)
		return output('False')
	
def getAllAnswersByQuestionId(request, questionID):
	try:
		dict_answers = global_answer_class.data.find_one({"questionID" : questionID})
		dict_id = dict_answers["id"]
		cursorList = []
		cursor_answers = global_answer_class.data.find({"answer" : dict_id})
		for x in range(0, cursor_answers.count(), 1):
			dico = cursor_answers[x]
			cursorList.append(dico["answer"])
		return JsonResponse(cursorList, safe = False)
	except Exception as e:
		print(e)
		return output('False')
